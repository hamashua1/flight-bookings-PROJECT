from django.shortcuts import render

# Create your views here.
def hello_world(request):
    from django.http import HttpResponse
    return HttpResponse("Hello World")
def hamashua(request):
    from django.http import HttpResponse
    return HttpResponse("Hello Hamashua")

