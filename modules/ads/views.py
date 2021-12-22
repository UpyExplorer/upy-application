from app.base import BaseUpy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from modules.ads.models import AdsLink
from django.utils.translation import gettext_lazy as _


class AdsListView(BaseUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'ads_list.html'
    model = AdsLink
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(AdsListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Ads')
        context['view_name'] = _('Ads List')
        context['view_info'] = _('Ads')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_ads_list'):
            raise PermissionDenied

        return AdsLink.objects.filter(company_data_id=self.company_id()).order_by('-id').all()
