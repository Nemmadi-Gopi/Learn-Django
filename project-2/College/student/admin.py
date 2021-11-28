from django.contrib import admin
from student.models import AuthorModel, publishermodel, BookModel, MyUser
# Register your models here.
admin.site.register(AuthorModel)
admin.site.register(publishermodel)
admin.site.register(BookModel)
admin.site.register(MyUser)