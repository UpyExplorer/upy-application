from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(LoginRequiredMixin, TemplateView):
    template_name = 'main/change_language.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.language_view'):
            raise PermissionDenied

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
