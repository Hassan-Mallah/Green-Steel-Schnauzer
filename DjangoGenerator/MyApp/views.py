from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_generator():
    x = 0
    while True:
        yield x
        x += 1


my_g = my_generator()


def home(request):
    return HttpResponse(next(my_g))