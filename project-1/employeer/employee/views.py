from django.shortcuts import render
from django.http import HttpResponse
from employee.forms import SigninForm
# Create your views here.

def home(request):
    return HttpResponse("hello, Django..This is my first programme!")

def signup(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_bound:
            if form.is_valid():
                fname = form.cleaned_data.get['firstname']
                lname = form.cleaned_data.get['lastname']
                uname = form.cleaned_data.get['username']
                pswd = form.cleaned_data.get['password']
                email = form.cleaned_data.get['email']
                phn_number = form.cleaned_data.get['phone_number']
                dob = form.cleaned_data.get['dob']



