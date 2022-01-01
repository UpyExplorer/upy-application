# coding=utf-8

"""
Module Docstring
"""

from app.base import BaseViewUpy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from modules.seller.models import Seller
from django.utils.translation import gettext_lazy as _


class SellerListView(BaseViewUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'seller_list.html'
    model = Seller
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(SellerListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Seller')
        context['view_name'] = _('Seller List')
        context['view_info'] = _('Seller')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_seller_list'):
            raise PermissionDenied

        return Seller.objects.filter(company_data_id=self.company_id()).order_by('-id').all()
