from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_generator():
    x = 0
    while x < 5:
        yield x
        x += 1

def home(request):
    return HttpResponse(my_generator())