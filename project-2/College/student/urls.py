
from django.contrib import admin
from django.urls import path
from student import views


urlpatterns = [
    path('home/', views.home, name ="home-path"),
    path('signup/', views.Signup_details, name='signup_details'),
]
