from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,Group, Permission
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, password, firstname, lastname, **extra_fields):
        if not username:
            raise ValueError('The user must have an username')
        if not password:
            raise ValueError('The user must have a password')
        if not firstname:
            raise ValueError('The user must have a full name')

        if not lastname:
            raise ValueError('The user must have a phone number')

        username = self.normalize_username(username)
        user = self.model(username=username, firstname=firstname, lastname=lastname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, firstname, lastname, **extra_fields):
        """
        Create and save a SuperUser with the given email, fullname, phone and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(self, username, password, firstname, lastname, **extra_fields)



class MyUser(AbstractBaseUser):
    firstname = models.CharField(max_length=255, blank=False, null=False)
    lastname = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser =  models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        username = '%s' % (self.username)
        return username

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