from django import forms
from django.contrib.auth.models import User
from django.forms import fields


class SigninForm(forms.ModelForm):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length=255)
    phone_number = forms.IntegerField(max_length = 100)
    dob = forms.DateField()
    class meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'password', 'email', 'phone_number', 'dob']

