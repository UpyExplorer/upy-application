from django.views import generic
from django.shortcuts import Http404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, View
from modules.catalog.product.forms import ProductForm
from modules.catalog.product.models import Product
from modules.utils import get_company_id


class ProductListView(LoginRequiredMixin, generic.ListView):
    template_name = 'catalog/product/product_list.html'
    model = Product
    paginate_by = 5

    def get_queryset(self):
        company_data_id = get_company_id(self.request.user.id)
        return Product.objects.filter(company_data_id=company_data_id).all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['view_path'] = 'Dashboard / Catalog / Product'
        context['view_name'] = 'Product List'

        return context


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'catalog/product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['view_path'] = 'Dashboard / Catalog / Product / View'
        context['view_name'] = 'Product View'

        return context

    def get_object(self):
        company_data_id = get_company_id(self.request.user.id)
        product = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=company_data_id).first()

        if not product:
            raise Http404('Product does not exist')

        return product

class ProductFormView(LoginRequiredMixin, View):
    template_name = 'catalog/product/product_edit.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super(ProductFormView, self).get_context_data(**kwargs)
        context['view_path'] = 'Dashboard / Catalog / Product / Edit'
        context['view_name'] = 'Product Edit'

        return context

    def get(self, *args, **kwargs):
        company_data_id = get_company_id(self.request.user.id)
        instance = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=company_data_id).first()
        form = ProductForm(instance=instance)
        return render(self.request, self.template_name, {"form": form})

    def post(self, *args, **kwargs):
        company_data_id = get_company_id(self.request.user.id)
        instance = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=company_data_id).first()

        if self.request.method == "POST":
            if instance:
                form = self.form_class(self.request.POST, instance=instance)
            else:
                form = self.form_class(self.request.POST) 
            form.save()
            return redirect('catalog:product_list')
        return redirect('catalog:product_list')


# class ProductFormView(LoginRequiredMixin, FormView):
#     template_name = 'catalog/product/product_edit.html'
#     form_class = ProductForm
#     success_url = '/catalog/product/'

    # def __init__(self, *args, **kwargs):
    #     super().__init__()

    # def get_initial(self):
    #     company_data_id = get_company_id(self.request.user.id)
    #     self.product = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=company_data_id).first()
    #     initial = super().get_initial()
    #     initial['name'] = self.product.name
    #     initial['sku'] = self.product.sku
    #     return initial

    # def form_valid(self, form):
    #     self.product.name = form.cleaned_data['name']
    #     self.product.sku = form.cleaned_data['sku']
    #     self.product.save()

    #     return redirect('catalog:product_list')