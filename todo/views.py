from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse

def todo(request):
    return HttpResponse(b'Hello World')
