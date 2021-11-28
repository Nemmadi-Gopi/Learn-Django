from django.db import models
from datetime import date
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission, UserManager
from django.contrib.auth import get_user_model

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password, **extra_fields):
        if not firstname:
            raise ValueError('The user must have an firstname')
        if not lastname:
            raise ValueError('The user must have an lastname')
        if not email:
            raise ValueError('The user must have an email')
        if not password:
            raise ValueError('The must have a password')


        
        email = self.normalize_email(email)
        user = self.model(firstname = firstname, lastname = lastname, email = email, **extra_fields)            
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, firstname, lastname, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(firstname, lastname, email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):

    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    # is_superuser field provided by PermissionsMixin if we use PermissionsMixin
    # groups field provided by PermissionsMixin if we use PermissionsMixin
    # user_permissions field provided by PermissionsMixin if we use PermissionsMixin


    firstname = models.CharField(max_length=255, blank=False, null=False)
    lastname = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique = True, max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    dob = models.DateField(blank=True, null = True)
    bio = models.TextField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    # def __str__(self):
    #     return self.email
        
    def __str__(self):
        email = '%s' % (self.email)
        return email
    def get_firstname(self):
        return self.firstname.strip()
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_perms(self, perm_list, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def email_user(self):pass

    def get_user_permissions(self):pass

    def get_group_permissions(self):pass

    def get_all_permissions(self):pass

class AuthorModel(models.Model):
    name = models.CharField(max_length=50, blank=False, null = False)
    email = models.EmailField(max_length=150, blank=True, null = True)
    st_date = models.DateField()

    def __str__(self):
        return self.name

class publishermodel(models.Model):
    author = models.ManyToManyField(AuthorModel)
    name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    pub_date = models.DateField()

    def __str__(self):
        return self.name

class BookModel(models.Model):
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    B_name = models.CharField(max_length=255)
    pages = models.IntegerField(verbose_name='number of pages')
    price  = models.DecimalField(max_digits=30, decimal_places=2, verbose_name='price')
    release_date = models.DateField()

    def __str__(self):
        return self.B_name