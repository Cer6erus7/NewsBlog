from django.shortcuts import render
from .models import *


def home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {"post": post})


def page(request, id):
    post_page = Post.objects.get(id=id)
    comments = Category.objects.get
    return render(request, 'page.html', {"post_page": post_page})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')