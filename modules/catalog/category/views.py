# coding=utf-8

"""
Module Docstring
"""

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _

from modules.catalog.category.models import Category
from app.base import BaseViewUpy



class CategoryListView(BaseViewUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'catalog/category/category_list.html'
    model = Category
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Catalog / Category')
        context['view_name'] = _('Category List')
        context['view_info'] = _('Category')
        context['btn_info'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_catalog_category_list'):
            raise PermissionDenied

        return Category.objects.filter(company_data_id=self.company_id()).order_by('-id').all()
