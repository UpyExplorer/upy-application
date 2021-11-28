from django.views import generic
from django.shortcuts import Http404, render
from modules.product.models import Info

class ProductListView(generic.ListView):
    model = Info
    template_name = 'product/product_list.html'

    def get_queryset(self):
            return Info.objects.all()[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProductListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class ProductDetailView(generic.DetailView):
    model = Info

    def book_detail_view(request, primary_key):
        try:
            book = Info.objects.get(pk=primary_key)
        except Info.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'product/product_detail.html', context={'book': book})