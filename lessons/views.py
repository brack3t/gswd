from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView

from braces.views import SelectRelatedMixin, SetHeadlineMixin

from lessons.models import Lesson


class LessonListView(SetHeadlineMixin, SelectRelatedMixin, ListView):
    headline = _("Lessons")
    model = Lesson
    select_related = ["transcripts"]


class LessonDetailView(SelectRelatedMixin, DetailView):
    model = Lesson
    select_related = ["transcripts"]


class LessonSearchView(SetHeadlineMixin, ListView):
    model = Lesson
    template_name = "lessons/lesson_list.html"

    def get_headline(self):
        return _('Search results for "%s"' % self.request.REQUEST.get("q"))

    def get_queryset(self):
        query = self.request.REQUEST.get("q")
        return self.model.objects.select_related("transcripts").filter(
            Q(title__icontains=query) |
            Q(transcripts__intro__icontains=query) |
            Q(transcripts__body__icontains=query) |
            Q(transcripts__transcript__icontains=query)
        )
