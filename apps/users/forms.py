from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.users.models import CustomUser


class UserFrom(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'display_name', 'avatar']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'display_name',
            'avatar'
        )