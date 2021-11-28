from django.views import generic
from django.shortcuts import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from modules.catalog.models import Product
from modules.utils import get_company_id


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = 'catalog/product/product_list.html'
    paginate_by = 5

    def get_queryset(self):
        company_data_id = get_company_id(self.request.user.id)
        return Product.objects.filter(company_data_id=company_data_id).all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'catalog/product/product_detail.html'

    def get_object(self):
        company_data_id = get_company_id(self.request.user.id)
        product = Product.objects.filter(pk=self.kwargs['pk'], company_data_id=company_data_id).first()

        if not product:
            raise Http404('Product does not exist')

        return product
