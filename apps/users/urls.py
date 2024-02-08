from django.urls import path

from apps.users.views import SignUpView,


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('update-user/<int:pk>',UserUpdateView.as_view(), name="update_user")
]
