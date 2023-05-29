from django.shortcuts import render
from .models import *
from .forms import *


def home(request):
    post = Post.objects.all()
    return render(request, 'index.html', {"post": post})


def page(request, id):
    post_page = Post.objects.get(id=id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        data = form.save(commit=False)
        data.post = post_page
        data.save()

    return render(request, 'page.html', {"post_page": post_page, 'form': form})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')