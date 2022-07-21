from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from college_app.models import Student_Detail
from django.contrib import messages
from datetime import date
import re
from django.contrib.auth import authenticate, login, logout
import uuid


UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)




def verify_key_view(request):

    if request.method == 'POST':
        verify_key = request.POST['verify']
        if UUID_PATTERN.match(verify_key):

            try:
                detail = Student_Detail.objects.get(unique_id1 = verify_key)

                return redirect('/verify/key/' + str(verify_key))


            except :
                return HttpResponse('<h1>Key Not Exist</h1>')
            
        else:
            return render(request,'index.html',{'message': 'Please Enter Valid Verification Key'})



def certificate_view(request,verify_key):
        
            try:
                detail = Student_Detail.objects.get(unique_id1 = verify_key)

                if detail.event=='competition':
                    if detail.position_category=='Secured Rank':
                        return render(request,"01_verify.html", {'student_name': detail.student_name,
                        'college_name': detail.college_name,
                        'event': detail.event,
                        'position_category': detail.position_category,
                        'position':detail.position,
                        'event_name':detail.event_name,
                        'about_event':detail.about_event,
                        'certification_date':detail.certification_date,
                        'email':detail.email1,
                        'unique_id' : detail.unique_id1})

                    elif detail.position_category=='Participation':
                        return render(request,"02_verify.html", {'student_name': detail.student_name,
                        'college_name': detail.college_name,
                        'event': detail.event,
                        'position_category': detail.position_category,
                        'event_name':detail.event_name,
                        'about_event':detail.about_event,
                        'certification_date':detail.certification_date,
                        'email':detail.email1,
                        'unique_id' : detail.unique_id1})

                elif detail.event=='workshop':
                        return render(request,"03_verify.html", {'student_name': detail.student_name,
                        'college_name': detail.college_name,
                        'event': 'Workshop',
                        'certification_date':detail.certification_date,
                        'event_name':detail.event_name,
                        'about_event':detail.about_event,
                        'email':detail.email1,
                        'unique_id' : detail.unique_id1})
            except:
                return HttpResponse("<h1>Don't be oversmart<h1>")