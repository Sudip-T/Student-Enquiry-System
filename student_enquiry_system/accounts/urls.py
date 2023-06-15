from django.urls import path
from .views import LoginView, RegistrationView, LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .views import profile



urlpatterns = [
    path('login/', LoginView.as_view(), name='log_in'),
    path('logout/', LogoutView.as_view(), name='log_out'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('password-change/', PasswordChangeView.as_view(template_name='accounts/password_change.html', success_url=reverse_lazy('dashboard')), name='password_change'),
    path('profile/', profile, name='profile' ),
]