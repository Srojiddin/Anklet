from django.views import generic

from apps.categories.models import Category
from apps.products.models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"

