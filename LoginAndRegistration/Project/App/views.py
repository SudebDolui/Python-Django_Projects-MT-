from django.shortcuts import render

# Create your views here.

def home(req):
    render(req, 'home.html')