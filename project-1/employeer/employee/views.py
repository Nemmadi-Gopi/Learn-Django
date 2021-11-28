from django import http
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee import forms
from employee.models import User, AuthorModel, BookModel, publishermodel
from django.contrib.auth import login, authenticate, logout  # add to imports
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Signupview(request):
    if request.method == 'POST':
        form = forms.SigninForm(data = request.POST)
        if form.is_bound:
            if form.is_valid():
                form.save()
                # firstname = form.cleaned_data['firstname']
                # lastname = form.cleaned_data['lastname']
                # email= form.cleaned_data['email']
                # password = form.cleaned_data['password']
                # dob = form.cleaned_data['dob']


                # user = User.object.create_user(firstname, lastname, email, dob)
                # user.is_active = True
                # user.psd = password
                # user.save()

                return redirect('login')
            else:
                return HttpResponse("data is invalid")
        else:
            return HttpResponse('Form is having no data')
    else:
        form = forms.SigninForm()
        return render(request, 'signup.html', {'form': form})



def loginview(request):
    if request.method == 'POST':
        form = forms.Loginform(data = request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            psd= form.cleaned_data.get('password')
            user = authenticate(request = request, email = email, password = psd)
            if user is not None:
                login(request, user)
                return HttpResponse('invalid')
            else:
                return redirect('book_list')
        else:
            return HttpResponse('invalid data')
    else:
        form = forms.Loginform()
    return render(request, 'login.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('login')

def listAuthors(request):
    data = AuthorModel.objects.all()

    return render(request, 'author_details.html', {'Data': data})


def listbook(request):
    data = BookModel.objects.all()
    return render(request, 'book_details.html', {'Data': data})

def listpublisher(request):
    data = publishermodel.objects.all()
    return render(request, 'publisher_details.html', {'Data': data})
    



# def add_authorview(request):
#     if request.method =='POST':
#         form = forms.AuthorForm(request.POST)
#         if form.is_bound:
#             if form.is_valid():
#                 form.save()
#                 return redirect('author_details')
#             else:
#                 return HttpResponse('form is invalid')
#         else:
#             return HttpResponse('invalid data')
#     else:
#         form = forms.AuthorForm()
#     return render(request, {'form': form})


