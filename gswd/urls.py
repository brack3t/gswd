from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from gswd.views import LogoutView, HomeView

urlpatterns = patterns('',
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),
    url(r'^$', HomeView.as_view(), name="home"),
)

urlpatterns += staticfiles_urlpatterns()
