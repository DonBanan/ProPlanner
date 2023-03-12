from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
