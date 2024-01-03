from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "author": "CoreyMs",
        "title": "Blog Post 1",
        "content": "First Post",
        "data_posted": "August 2015",
    },
    {
        "author": "lorem",
        "title": "Blog Post 2",
        "content": "First Post",
        "data_posted": "August 2015",
    },
    {
        "author": "lorem3",
        "title": "Blog Post 3",
        "content": "First Post",
        "data_posted": "August 2015",
    },
    {
        "author": "lorem3",
        "title": "Blog Post 4",
        "content": "First Post",
        "data_posted": "August 2015",
    },
]


def home(request):
    context={
        'posts': posts
    }
    return render(request, "blog/home.html",context)


def about(request):
    return render(request, "blog/about.html")
