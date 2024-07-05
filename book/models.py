from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia


class Auther(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Auther, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to=SaveMedia.save_image, null=True)
    count = models.PositiveIntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}'

# Create your models here.
