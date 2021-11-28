from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, help_text='Last Name')
#     last_name = forms.CharField(max_length=100, help_text='Last Name')
#     email = forms.EmailField(max_length=150, help_text='Email')


#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email','password')
#         exclude = ['password confimation']