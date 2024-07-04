from django.urls import path
from .views import home,login,register,books,auther
urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('books/',books,name='books'),
    path('auther/',auther,name='auther'),


]