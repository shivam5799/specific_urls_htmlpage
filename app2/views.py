from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sample1(request):
    return HttpResponse('<h1>sample1 of app2</h1>')

def sample2(request):
    return HttpResponse('<h1>Sample2 of app2</h1>')