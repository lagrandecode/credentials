from django.shortcuts import render

# Create your views here.

def registerview(request):
    return render(request, 'register.html')
