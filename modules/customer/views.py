# coding=utf-8

"""
Module Docstring
"""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

from modules.customer.models import Customer
from app.base import BaseViewUpy


class CustomerListView(BaseViewUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'customer_list.html'
    model = Customer
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Customer')
        context['view_name'] = _('Customer List')
        context['view_info'] = _('Customer')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_customer_list'):
            raise PermissionDenied

        return Customer.objects.filter(company_data_id=self.company_id()).order_by('-id').all()
