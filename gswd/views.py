from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, RedirectView

from braces.views import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "index.html"
