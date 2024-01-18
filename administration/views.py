from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt


def admin1(request):
    return HttpResponse("Hello, world. You're at administration1.")

def admin2(request):
    context = { 
        'variable1': 'Hello',
        'variable2': 'World',
    }
    return render(request, 'my_template.html', context)

@csrf_exempt
def addition(request):
    if request.method == 'POST':
        num1 = request.POST.get('number1',0)
        num2 = request.POST.get('number2',0)
        result = int(num1) + int(num2)
        return HttpResponse(result)
    else:
        return render(request, 'addition.html')
    
 
def admin3(request):
    return HttpResponse("Hello, world. You're at administration3.")