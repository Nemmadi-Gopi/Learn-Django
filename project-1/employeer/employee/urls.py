from django.contrib import admin
from django.urls import path
from employee import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.Signupview, name = 'signup'),
    path('login/', views.loginview, name = 'login'),
    path('logout/', views.signout, name = 'logout'),
    path('authors_list/', views.listAuthors, name = 'authors_list'),
    path('book_list/', views.listbook, name = 'book_list'),
    path('publisher_list/', views.listpublisher, name = 'publisher_list'),   
]

