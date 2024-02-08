from django.contrib.auth.forms import UserCreationForm

from apps.users.models import CustomUser


class UserFrom(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'display_name','avatar']

# class SignUpForm(CreateView):