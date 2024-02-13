from django.views.generic import CreateView, UpdateView

from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from apps.products.models import Product
from apps.users.forms import UserFrom, UserUpdateForm

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = UserFrom
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('products_list')
    template_name = 'update-profile.html'


