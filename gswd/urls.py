from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gswd.views.home', name='home'),
    # url(r'^gswd/', include('gswd.foo.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),
)

urlpatterns += staticfiles_urlpatterns()
