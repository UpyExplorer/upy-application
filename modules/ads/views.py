# coding=utf-8

"""
Module Docstring
"""

from app.base import BaseViewUpy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from modules.ads.models import AdsLink
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect, render
from modules.ads.forms import AdsLinkForm


class AdsListView(BaseViewUpy, LoginRequiredMixin, generic.ListView):
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


class AdsUpdateView(BaseViewUpy, LoginRequiredMixin, generic.UpdateView):
    template_name = 'ads_update.html'
    form_class = AdsLinkForm
    model = AdsLink

    def get_object(self):
        product = AdsLink.objects.filter(pk=self.kwargs['pk'], company_data_id=self.company_id()).first()

        return product

    def get(self, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_ads_update'):
            raise PermissionDenied

        object = self.get_object()

        if not object:
            messages.warning(self.request, _('Ads not found!'))
            return redirect('ads:ads_list')

        return render(self.request, self.template_name, {
				"object": object,
				"form": AdsLinkForm(instance=object),
				"view_path": _('Dashboard / Ads'),
				"view_name": _('Ads Edit'),
                "view_info": _('Ads'),
                "btn_info": True,
                "btn_save": True,
                "btn_delete": True
			}
		)

    def post(self, request, *args, **kwargs):
        messages.success(request, _('Ads saved successfully!'))
        return super().post(request, *args, **kwargs)
