# coding=utf-8

"""
View Application
"""

from app.base import BaseUpy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.views import generic

from modules.application.models import BaseApplication


class ApplicationListView(BaseUpy, LoginRequiredMixin, generic.ListView):
    """
    List View Application
    """
    template_name = 'application_list.html'
    model = BaseApplication
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ApplicationListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Application')
        context['view_name'] = _('Application List')
        context['view_info'] = _('Application')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_application_list'):
            raise PermissionDenied

        return BaseApplication.objects.filter(status=True).order_by('id').all()
