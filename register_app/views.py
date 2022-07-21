from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
import re
from django.contrib.auth import authenticate, login, logout
import uuid


def regsiter_view(request):            #Show register page
    return render(request, 'register.html') 



def register(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            if password == cpassword:
                user = User.objects.create_user(username, '', password)
                user.save()
                return redirect('/')
            else:
                return render(request, 'register.html', {'message': 'Password miss matched'})

    except:
        print("Username exist")
        # return redirect('/login/register_page',{'message': 'Username alredy exist'}) 
        return HttpResponse('<h1>User Already Exist')
        

    return render(request, 'register.html') #index.html
