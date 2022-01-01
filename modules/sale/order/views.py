# coding=utf-8

"""
Module Docstring
"""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

from modules.sale.models import Order
from app.base import BaseViewUpy



class OrderListView(BaseViewUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'order/order_list.html'
    model = Order
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Sale / Order')
        context['view_name'] = _('Order List')
        context['view_info'] = _('Order')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_sale_order_list'):
            raise PermissionDenied

        return Order.objects.filter(company_data_id=self.company_id()).order_by('-id').all()
