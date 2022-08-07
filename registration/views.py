

from django.shortcuts import render, redirect
from django.contrib.auth.models import authenticate, login, User
from django.contrib import messages

# Create your views here.

def registerview(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            user = User.objects.create_user(firstname=firstname,username=username,email=email,password=password)
            if user.is_valid():
                user.save()
                return redirect('home')
        else:
            messages.info(request,'password not matching')
            return redirect('/')





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