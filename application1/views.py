from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request):
    return HttpResponse("welcome to python")

def kishore(request):
    return HttpResponse("hello kishore")
def fullname(request):
    firstname = input("enter your first name: ")
    secondname= input("enter your second name: ")
    return HttpResponse(f"yourfull name is:{firstname+secondname}")