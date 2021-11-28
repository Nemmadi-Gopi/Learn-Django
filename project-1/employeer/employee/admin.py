from django.contrib import admin
from employee.models import User, AuthorModel, BookModel, publishermodel
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import AdminUserChangeForm, AdminUserCreationForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = AdminUserChangeForm
    add_form = AdminUserCreationForm
    
    list_display = ['firstname', 'lastname', 'email', 'password', 'dob','is_active', 'is_superuser']
    list_display_links = ['firstname','email']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    fieldsets = (
    (None, {'fields': ('firstname', 'lastname','email', 'password')}),
    ('Personal info', {'fields': ('dob', 'bio')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'firstname', 'lastname', 'email', 'password', 'dob', 'bio','is_active', 'is_staff','is_superuser')}
         ),
    )

    search_fields = ['firstname', 'lastname', 'email']
    ordering = ['email']
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(publishermodel)


