from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from .forms import EmailAuthenticationForm


class UserLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'auth/login.html'


class UserLogoutView(LogoutView):
    template_name = 'auth/logout.html'
