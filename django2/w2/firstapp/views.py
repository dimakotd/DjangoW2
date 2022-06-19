from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

  
def hellodjango(request):
    return HttpResponse("Hello Django!")

def helloname(request, name):
    return HttpResponse(f"Hello {name}!")

def about(request):
    return HttpResponse("This page is About!")

def printdate(request, name = ''):
    current_date =list(reversed(str(date.today()).split('-')))
    if name == '':
        return HttpResponse('.'.join(current_date))
    if name == 'day':
        return HttpResponse(current_date[0])
    if name == 'month':
        return HttpResponse(current_date[1])
    if name == 'year':
        return HttpResponse(current_date[2])
    
