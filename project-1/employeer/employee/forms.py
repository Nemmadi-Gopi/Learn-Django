from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from employee import models
from employee.models import User, AuthorModel
from django.contrib.auth.forms import ReadOnlyPasswordHashField


#create your form here..
class AdminUserCreationForm(forms.ModelForm):
    password = forms.CharField(required= True)

    class Meta:
        model = User
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': True})
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class SigninForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'password', 'dob', 'bio', 'is_active', 'is_staff']
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        us = User.object.filter(email = email)
        if us.exists():
            raise forms.ValidationError("email is taken")
        return email
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class AdminUserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'password', 'dob', 'bio', 'is_active', 'is_staff')
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class Loginform(forms.Form):
    email = forms.EmailField(max_length = 255)
    passcode = forms.CharField(max_length=60)

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = AuthorModel
        fields = '__all__'