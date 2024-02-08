from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from apps.users.forms import UserFrom

User = get_user_model()


class SignUpView(CreateView):
    model = User
    form_class = UserFrom
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
