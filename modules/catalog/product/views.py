from app.base import BaseViewUpy
from django.views import generic
from django.shortcuts import Http404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from modules.catalog.product.forms import ProductForm
from modules.catalog.product.models import Product
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from bootstrap_modal_forms.generic import BSModalDeleteView


class ProductListView(BaseViewUpy, LoginRequiredMixin, generic.ListView):
    template_name = 'catalog/product/product_list.html'
    model = Product
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Catalog / Product')
        context['view_name'] = _('Product List')
        context['view_info'] = _('Product')
        context['btn_info'] = True
        context['btn_create'] = True

        return context

    def get_queryset(self):
        if not self.request.user.has_perm('global_permissions.app_catalog_product_list'):
            raise PermissionDenied

        return Product.objects.filter(company_data_id=self.company_id()).order_by('-id').all()


class ProductDetailView(BaseViewUpy, LoginRequiredMixin, generic.DetailView):
    template_name = 'catalog/product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_catalog_product_detail'):
            raise PermissionDenied

        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Catalog / Product')
        context['view_name'] = _('Product View')
        context['view_info'] = _('Product')
        context['btn_info'] = True

        return context

    def get_object(self):
        object = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=self.company_id()).first()

        if not object:
            raise Http404('Product does not exist')

        return object


class ProductUpdateView(BaseViewUpy, LoginRequiredMixin, generic.UpdateView):
    template_name = 'catalog/product/product_update.html'
    form_class = ProductForm
    model = Product

    def get_object(self):
        product = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=self.company_id()).first()

        return product

    def get(self, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_catalog_product_update'):
            raise PermissionDenied

        object = self.get_object()

        if not object:
            messages.warning(self.request, _('Product not found!'))
            return redirect('catalog:product_list')

        return render(self.request, self.template_name, {
				"object": object,
				"form": ProductForm(instance=object),
				"view_path": _('Dashboard / Catalog / Product'),
				"view_name": _('Product Edit'),
                "view_info": _('Product'),
                "btn_info": True,
                "btn_save": True,
                "btn_delete": True
			}
		)

    def post(self, request, *args, **kwargs):
        messages.success(request, _('Product saved successfully!'))
        return super().post(request, *args, **kwargs)

class ProductCreateView(BaseViewUpy, LoginRequiredMixin, generic.CreateView):
    template_name = 'catalog/product/product_update.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_catalog_product_create'):
            raise PermissionDenied

        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['view_path'] = _('Dashboard / Catalog / Product')
        context['view_name'] = _('Product View')
        context['view_info'] = _('Product')
        context['btn_info'] = True
        context['btn_save'] = True

        return context

    def post(self, request, *args, **kwargs):
        if self.request.method == "POST":
            form = self.form_class(self.request.POST)
            object = form.save()

            product = Product.objects.get(id=object.id)
            product.company_data_id = self.company_id()
            product.save()

            messages.success(request, _('Product saved successfully!'))
            return redirect(product.get_absolute_url())

        return redirect('catalog:product_list')


class ProductDeleteView(BaseViewUpy, LoginRequiredMixin, BSModalDeleteView):
    model = Product
    template_name = 'catalog/product/product_delete.html'
    success_url = '/catalog/product'
    success_message = _('Product was deleted')

    def get_object(self):
        product = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=self.company_id()).first()

        return product

    def get(self, request, *args, **kwargs):
        if not self.request.user.has_perm('global_permissions.app_catalog_product_delete'):
            raise PermissionDenied
    
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)