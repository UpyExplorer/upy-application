from django.views import generic
from django.shortcuts import Http404, render
from modules.catalog.models import Product

class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product/product_list.html'

    def get_queryset(self):
            return Product.objects.all()[:5]

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product/product_detail.html'

    def book_detail_view(request, primary_key):
        try:
            product = Product.objects.get(pk=primary_key)
        except Product.DoesNotExist:
            raise Http404('Product does not exist')

        return render(request, context={'product': product})