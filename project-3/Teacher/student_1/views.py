from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm



from django.contrib.auth import login, authenticate



# from student_1.models import Profile
from .forms import SignUpForm
# Create your views here.

def home(request):
    return HttpResponse("<h1>hello, Django..This is my first programme!</h1>")


def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("User has been created successfully")
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password1')
        # user = authenticate(username=username, password=password)
        # login(request, user)
        # return redirect('home')
    return render(request, 'signup.html', {'form': form})

# def Signupview(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_bound:
#             if form.is_valid():
#                 emailid = form.cleaned_data['email']
#                 fname = form.cleaned_data['first_name']
#                 lname = form.cleaned_data['last_name']
#                 uname = form.cleaned_data['username']
#                 psd = form.cleaned_data['password']
#                 user = User.objects.create(email = emailid, first_name = fname, last_name = lname, username = uname)
#                 print(user)
#                 user.setpassword = psd
#                 user.save()
#                 return HttpResponse('user created successfully')
#             else:
#                 return HttpResponse("No data is found")
#         else:
#             return HttpResponse('not bound')
#     else:
#         form = SignUpForm()
#         return render(request,'signup.html', {'form': form})
