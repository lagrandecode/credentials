

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def registerview(request):
    return render(request, 'register.html')



def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')





def logout(request):
    logout(request)
    return render(request, 'login.html')