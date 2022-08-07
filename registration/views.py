

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def registerview(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name)
                if user.is_valid():
                    user.save()
                    print(user)
                    return redirect('login')
        else:
            messages.info(request,'password not matching')
            print(messages)
            return redirect('register')
    return render(request, 'register.html')



def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')





def logoutview(request):
    auth.logout(request)
    return redirect('home')