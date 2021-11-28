from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.forms import fields
from .models import MyUser

class SignupForm(forms.ModelForm):
    # firstname = forms.CharField(max_length=255, blank=False, null=False)
    # lastname = forms.CharField(max_length=255, blank=False, null=False)
    # username = forms.CharField(max_length=255, blank=False, null=False)
    # password = forms.CharField(max_length=255, blank=False, null=False)
    # dob = forms.DateField()

    class Meta:
        model = MyUser
        fields = '__all__'
        exclude = ('Last login',)