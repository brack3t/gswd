from django.views.generic import ListView, DetailView

from braces.views import SelectRelatedMixin

from gswd.utils import get_redis_connection
from qa.models import Answer, Question


class QuestionListView(SelectRelatedMixin, ListView):
    model = Question
    select_related = ["user"]


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        """
        Get answer rankings from Redis and return a sorted list of
        answers in the context.
        """
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        obj = self.get_object()
        red = get_redis_connection()

        ranked_pk_list = red.zrevrange(obj.redis_key, 0, -1)

        if not ranked_pk_list:
            return context

        answers = Answer.objects.in_bulk(ranked_pk_list)

        context.update({"ranked_answers": [
            answers[int(rank)] for rank in ranked_pk_list]})

        return context
