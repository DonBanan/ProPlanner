from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView

from .models import User
from .forms import EmailAuthenticationForm


class UserLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'auth/login.html'


class UserLogoutView(LogoutView):
    template_name = 'auth/logout.html'


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'

    def test_func(self):
        """Проверяем, что текущий пользователь является владельцем профиля"""
        profile = self.get_object()
        return self.request.user == profile


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'middle_name']
    template_name = 'profiles/profile_form.html'

    def test_func(self):
        """Проверяем, что текущий пользователь является владельцем профиля"""
        profile = self.get_object()
        return self.request.user == profile

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.kwargs['pk']})