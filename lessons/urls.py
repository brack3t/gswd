from django.conf.urls import patterns, url

from lessons.views import LessonListView, LessonDetailView

urlpatterns = patterns('',
    url(r'^$', LessonListView.as_view(), name="list"),
    url(r'^(?P<slug>[-_\w]+)/$', LessonDetailView.as_view(), name="detail"),
)
