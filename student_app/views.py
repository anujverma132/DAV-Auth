from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
from college_app.models import Student_Detail
import re
from django.contrib.auth import authenticate, login, logout
import uuid

# Create your views here.


def issued_certificate_list(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("/college/dashboard/")
        else:    
            user1 = request.user.email
            query_set = Student_Detail.objects.filter(email1 = user1)
            context = {
                'object_list' : query_set
            }
            return render(request,'user_dashboard.html',context)
    else:
        return redirect("/")
