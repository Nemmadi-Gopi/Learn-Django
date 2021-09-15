from django.db import models
from datetime import datetime

# Create your models here.
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



