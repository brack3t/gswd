from django.conf.urls import patterns, url

from qa.views import QuestionListView, QuestionDetailView

urlpatterns = patterns('',
    url(r"^$", QuestionListView.as_view(), name="list"),
    url(r"^(?P<slug>[-_\w]+)/$", QuestionDetailView.as_view(), name="detail"),
)
