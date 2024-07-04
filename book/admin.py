from django.contrib import admin
from .models import Book,Auther,Comment
admin.site.register(Book)
# admin.site.register(User)
admin.site.register(Auther)
admin.site.register(Comment)
# Register your models here.