from django.views.generic import ListView, DetailView

from braces.views import SelectRelatedMixin

from qa.models import Question


class QuestionListView(SelectRelatedMixin, ListView):
    model = Question
    select_related = ["user"]


class QuestionDetailView(SelectRelatedMixin, DetailView):
    model = Question
    select_related = ["user", "answers"]
