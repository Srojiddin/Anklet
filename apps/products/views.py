from django.views import generic

from apps.categories.models import Category
from apps.products.models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = "products"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['left_categories'] = Category.objects.filter(parent=None)
        context['palto_products'] = Product.objects.filter(category__title="Пальто")[:4]
        context['shtany_products'] = Product.objects.filter(category__title="Штаны")[:4]
        context['crossy_products'] = Product.objects.filter(category__title="Кроссы")[:4]


        return context


class ProductDetailView(generic.DetailView):
    model = Product
    pk_url_kwarg = 'slug'
    template_name = 'detail.html'