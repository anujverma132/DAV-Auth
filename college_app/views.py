from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from datetime import date
import re
from django.contrib.auth import authenticate, login, logout
import uuid


# Create your views here.

def dashboard(request):
    
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request,'college_dashboard.html')
        else:
            return redirect("/")



def student_detail_html(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            unique_key = uuid.uuid4()
            if request.method == 'POST':
                student_name1 = request.POST['student_name'] 
                college_name = request.POST['college_name'] 
                event = request.POST['event']
                position_category = request.POST['position_category']
                position = int(request.POST['position'] or 0)
                event_name = request.POST['event_name']
                about_event = request.POST['about_event']
                email1 = request.POST['email']
                certification_date = (request.POST['certification_date'] or date.today)


                certificate = Student_Detail.objects.create(student_name = student_name1,
                college_name = college_name,
                position = position,
                event = event,
                event_name = event_name,
                about_event = about_event,
                position_category = position_category,
                certification_date= certification_date,
                email1 = email1,
                unique_id1 = unique_key,
                issue_by = request.user,)
                return redirect("/college/finish/" + str(unique_key)+'/')
        return render(request, 'submit_data.html')






def finish_view(request,user1):
    if request.user.is_staff:
        return render(request,'finish.html', {'key': user1})