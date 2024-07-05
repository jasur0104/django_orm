from django.shortcuts import render
from .models import Book, Auther


def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def books(request):
    books = Book.objects.all()
    context = {'a_books': books}
    return render(request, 'books.html', context=context)


def auther(request):
    auther = Auther.objects.all()
    context = {'a_auther': auther}
    return render(request, 'auther.html', context=context)

# Create your views here.
