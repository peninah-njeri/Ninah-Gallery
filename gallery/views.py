from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse('God creates the beauty. My camera and i are a witness.')

