from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<doctype>...")


def about(request):
    return HttpResponse("<h1>About us</h1>")
