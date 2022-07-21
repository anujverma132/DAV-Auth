from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'index.html')


def login_page(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/college/dashboard/')
        else :
            return redirect("/user/user_certificate/")    
    return render(request,'login1.html')



def login1(request):         #authenticate user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                if request.user.is_staff:
                    return redirect('/college/dashboard')
                else:
                    return redirect('/user/user_certificate/')
    else:
        return redirect('/login/login_page')

def logout1(request):
    logout(request)
    return redirect('/')