from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.translation import ugettext_lazy as _
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

from gswd.views import LogoutView, HomeView

urlpatterns = patterns('',
    url(r"^pages/", include("django.contrib.flatpages.urls")),
    url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^grappelli/", include("grappelli.urls")),
    url(r'', include("social_auth.urls")),
    url(r"^i18n/", include("django.conf.urls.i18n")),
    url(r"^$", HomeView.as_view(), name="home"),

    (r"^questions/", include("qa.urls", namespace="qa")),
    (r"^resources/", RedirectView.as_view(url="/pages/gigantuan/",
        permanent=True)),
)

urlpatterns += i18n_patterns('',
    url(_(r"^logout/$"), LogoutView.as_view(), name="logout"),
    url(_(r"^lessons/"), include("lessons.urls", namespace="lessons")),
)

urlpatterns += staticfiles_urlpatterns()
