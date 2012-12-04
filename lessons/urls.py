from django.conf.urls import patterns, url

from lessons import views

urlpatterns = patterns('',
    url(r'^$', views.LessonListView.as_view(), name="list"),
    url(r'^search/$', views.LessonSearchView.as_view(), name="search"),
    url(r'^(?P<slug>[-_\w]+)/$', views.LessonDetailView.as_view(),
        name="detail"),
)
