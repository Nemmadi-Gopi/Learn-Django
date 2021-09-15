from django.contrib import admin
from employee.models import BookModel, AuthorModel, publishermodel
# Register your models here.
admin.site.register(BookModel)
admin.site.register(AuthorModel)
admin.site.register(publishermodel)

