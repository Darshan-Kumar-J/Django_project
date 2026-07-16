from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("hello world. you are at Darshan's home page")
    return render(request, 'website/home.html')

def about(request):
   # return HttpResponse("hello world. you are at Darshan's about page")
    return render(request, 'website/about.html')

def contact(request):
    #return HttpResponse("hello world. you are at Darshan's contact page")
    return render(request, 'website/contact.html')

def service(request):
    #return HttpResponse("hello world. you are at Darshan's service page")
    return render(request, 'website/service.html')