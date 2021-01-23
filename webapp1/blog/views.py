from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>This is what we do</h1>')

def contact (request):
    return HttpResponse('<h1>Call us on</h1>')
