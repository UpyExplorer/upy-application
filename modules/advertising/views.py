from app.base import BaseUpy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from modules.advertising.models import AdvertisingLink
from django.utils.translation import gettext_lazy as _


class AdvertisingListView(BaseUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'advertising_list.html'
    model = AdvertisingLink
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AdvertisingListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Advertising')
        context['view_name'] = _('Advertising List')
        context['view_info'] = _('Advertising')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_advertising_list'):
            raise PermissionDenied

        return AdvertisingLink.objects.filter(company_data_id=self.company_id()).order_by('-id').all()
