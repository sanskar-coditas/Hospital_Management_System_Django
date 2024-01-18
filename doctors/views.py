from django.shortcuts import render
from django.http import HttpResponse


def getDoc1(request):
    return HttpResponse("Hello, world. Its Doc1")

def getDoc2(request):
    return HttpResponse("Hello, world. Its Doc2")