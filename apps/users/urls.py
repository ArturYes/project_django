from django.urls import path
from django.views.decorators.cache import never_cache

from apps.users.apps import UsersConfig
from apps.users.views import UserLoginView, UserLogoutView, UserRegisterView, email_verification, UserUpdateView, \
    UserPasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', never_cache(UserLoginView.as_view()), name='login'),
    path('logout/', never_cache(UserLogoutView.as_view()), name='logout'),
    path('register/', never_cache(UserRegisterView.as_view()), name='register'),
    path('confirm-email/<str:token>/', never_cache(email_verification), name='confirm-email'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('recovery/', never_cache(UserPasswordResetView.as_view()), name='recovery')
]
