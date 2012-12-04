from django.contrib import messages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, RedirectView

from braces.views import LoginRequiredMixin


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        return reverse("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, _("You've been logged out. Come back soon!"))
        return super(LogoutView, self).get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "index.html"
