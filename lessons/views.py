from django.views.generic import ListView, DetailView

from braces.views import SelectRelatedMixin

from lessons.models import Lesson


class LessonListView(ListView):
    model = Lesson


class LessonDetailView(SelectRelatedMixin, DetailView):
    model = Lesson
    select_related = ["translations"]
