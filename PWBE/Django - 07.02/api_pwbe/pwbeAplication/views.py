from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def req(request):
    return HttpResponse("Request Funcionando!")
