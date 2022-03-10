from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = ('fio',)