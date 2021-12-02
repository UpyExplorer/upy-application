from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(LoginRequiredMixin, TemplateView):
    template_name = 'main/change_language.html'

    def get_context_data(self, **kwargs):
        context = super(ChangeLanguageView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Change Language')
        context['view_name'] = _('Change Language')

        return context

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_account_language_view'):
            raise PermissionDenied

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
