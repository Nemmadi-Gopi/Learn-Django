from django.contrib import admin
from django.urls import path
from . import forms
from employee import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.Signupview, name = 'signup'),
    path('login/', views.loginview, name = 'login'),
    path('logout/', views.signout, name = 'logout'),

    path('authors_list/', views.listAuthors, name = 'authors_list'),
    path('author/add/', views.addauthor, name='add-author'),
    path('edit_author/<str:pk>/', views.editauthor, name='edit_author'),
    path('delete_author/<str:pk>/', views.deleteauthor, name='delete_author'),

    path('book_list/', views.listbook, name = 'book_list'),
    path('books/add/', views.addbook, name='add-book'),
    path('edit_book/<str:pk>/', views.editbook, name='edit_book'),
    path('delete_book/<str:pk>/', views.deletebook, name='delete_book'),

    path('publisher_list/', views.listpublisher, name = 'publisher_list'),
    path('publisher/add/', views.addpublisher, name='add-publisher'),
    path('edit_publisher/<str:pk>/', views.editpublisher, name='edit_publisher'),
    path('delete_publisher/<str:pk>/', views.deletepublisher, name='delete_publisher'),

]

