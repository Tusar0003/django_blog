from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
