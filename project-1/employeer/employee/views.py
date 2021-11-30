from typing_extensions import OrderedDict
from django import http
from django.contrib import auth

from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee import forms
from employee.models import User, AuthorModel, BookModel, publishermodel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



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
    # current = request.user        # To find the current user details on another methods
    # print(current)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = forms.Loginform(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                # print(email)
                password = form.cleaned_data.get('password')
                # print(password)
                if email and password:
                    if not User.object.filter(email = email).exists():
                        return HttpResponse(email, "was not there users list")
                    else:
                        user = User.object.get(email = email)
                        if not check_password(password, user.password):
                            return HttpResponse("password is invalid")
                        else:
                            user = authenticate(request=request, email = email, password = password)
                            # print(user)
                            if user is not None:
                                login(request, user)
                                return redirect('home')
                            else:
                                return HttpResponse('login')
        else:
            form = forms.Loginform()
        return render(request, template_name='login.html', context= {'form': form})


# Login another model type
# def loginview(request):
#     if request.method == 'POST':
#         form = forms.Loginform(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             print(email)
#             password = form.cleaned_data.get('password')
#             print(password)
#             user = auth.authenticate(email = email, password = password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('book_list')
#             else:
#                 HttpResponse('login')
#     else:
#         form = forms.Loginform()
#     return render(request, template_name='login.html', context= {'form': form})
        



def signout(request):
    logout(request)
    return redirect('login')


@login_required
def listAuthors(request):
    data = AuthorModel.objects.all()
    return render(request, 'author_details.html', {'Data': data})


@login_required
def addauthor(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request = request, data = request.POST)
        if form.is_bound:
            if form.is_valid():
                form.save()
                return redirect('authors_list')
            else:
                return HttpResponse("form is invalid")
        else:
            return HttpResponse("No data")
    else:
        form = forms.AuthorForm()
    return render(request, 'add_author.html', {'form': form})

@login_required
def editauthor(request,pk):
    author = AuthorModel.objects.get(id = pk)
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST, instance=author)
        if form.is_bound:
            if form.is_valid():
                form.save()
                return redirect('authors_list')
            else:
                return HttpResponse("form is invalid")
        else:
            return HttpResponse("No data")   
    else:
        form = forms.AuthorForm(instance=author)
    return render(request, 'edit_author.html',  {'form': form})


@login_required
def deleteauthor(request, pk):
    author = AuthorModel.objects.get(id = pk)
    if request.method == 'POST':
        author.delete()
        return redirect('authors_list')
    else:
        context = {'item': author}
    return render(request, 'delete_author.html', context)



@login_required
def listbook(request):
    data = BookModel.objects.all()
    return render(request, 'book_details.html', {'Data': data})

@login_required
def addbook(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST)
        if form.is_bound:
            if form.is_valid():
                form.save()
                return redirect('authors_list')
            else:
                return HttpResponse("form is invalid")
        else:
            return HttpResponse("No data")
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def editbook(request,pk):
    book = BookModel.objects.get(id = pk)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book)
        if form.is_bound:
            if form.is_valid():
                form.save()
                return redirect('book_list')
            else:
                return HttpResponse("form is invalid")
        else:
            return HttpResponse("No data")   
    else:
        form = forms.BookForm(instance=book)
    return render(request, 'edit_book.html',  {'form': form})

@login_required
def deletebook(request, pk):
    book = BookModel.objects.get(id = pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    else:
        context = {'item': book}
    return render(request, 'delete_book.html', context)


@login_required
def listpublisher(request):
    data = publishermodel.objects.all()
    return render(request, 'publisher_details.html', {'Data': data})

@login_required
def addpublisher(request):
    if request.method == 'POST':
        form = forms.PublisherForm(request.POST)
        if form.is_bound:
            if form.is_valid():
                form.save()
                return redirect('publisher_list')
            else:
                return HttpResponse("form is invalid")
        else:
            return HttpResponse("No data")
    else:
        form = forms.PublisherForm()
    return render(request, 'add_publisher.html', {'form': form})

@login_required
def editpublisher(request,pk):
    publisher = publishermodel.objects.get(id = pk)
    if request.method == 'POST':
        form = forms.PublisherForm(request.POST, instance=publisher)
        if form.is_bound:
            if form.is_valid():
                form.save()
                return redirect('publisher_list')
            else:
                return HttpResponse("form is invalid")
        else:
            return HttpResponse("No data")   
    else:
        form = forms.PublisherForm(instance=publisher)
    return render(request, 'edit_publisher.html',  {'form': form})



@login_required
def deletepublisher(request, pk):
    publisher = publishermodel.objects.get(id = pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    else:
        context = {'item': publisher}
    return render(request, 'delete_publisher.html', context)


