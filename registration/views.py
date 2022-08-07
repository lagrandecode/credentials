from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def registerview(request):
    return render(request, 'register.html')



def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("USER",user)
        if user is not None:
            login(request, user)
            return redirect('home')
            print(user)
    else:
        return render(request, 'login.html')
