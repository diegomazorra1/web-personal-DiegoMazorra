from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request, 'base/portada.html')


def index(request):
    return render(request, 'base/base.html')


def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')
