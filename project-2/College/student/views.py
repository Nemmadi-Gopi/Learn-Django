from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import BookModel, AuthorModel, publishermodel, MyUser
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from student import forms
# Create your views here.
def home(request):
    return HttpResponse("this is the my project from django..!")

def Signup_details(request):
    if request.method =="POST":
        form = forms.SignupForm(data = request.POST)
        if form.is_bound:
            if form.is_valid():
                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                dob = form.cleaned_data['dob']
                user = MyUser.objects.create_user(firstname, lastname, username, dob)
                print(user)
                user.set_password(password)
                user.save()
                return HttpResponse("User created successfully")

    else:
        form = forms.SignupForm()
        return render(request, 'signup.html',{'form':form})