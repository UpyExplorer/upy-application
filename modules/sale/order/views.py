from app.base import BaseUpy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from modules.sale.models import Order
from django.utils.translation import gettext_lazy as _


class OrderListView(BaseUpy, LoginRequiredMixin, generic.ListView):
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
