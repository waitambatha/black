from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def websites(request):
    return render (request, 'websites.html')


def application(request):
 return render(request,'application.html')

def cyber_security(request):
    return render(request,'cyber_security.html')

def database(request):
    return render(request, 'database.html')

def software(request):
    return render(request,'software.html')

def profolio(request):
    return render(request,'profolio.html')

