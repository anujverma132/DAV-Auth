from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
import uuid 

# Create your models here.



class Student_Detail(models.Model):

    student_name = models.CharField(max_length= 20, help_text= 'Input Candidate Name')
    college_name = models.CharField(max_length= 50, help_text= 'Input College Name Who issue Certificate' )


    event = models.CharField(max_length= 12, default = "COMPETITION", help_text = 'Select Valid Choice' ) #choices = event_choices,
    
    event_name = models.CharField(max_length = 100)
    about_event = models.CharField(max_length = 100, help_text= 'About Certification')
        


    position_category = models.CharField(max_length= 20, default = "Participation", null=True,blank=True ,help_text = 'Select Valid Choice' )
    position = models.PositiveIntegerField(blank=True, help_text= 'Input Position', null=True)

    


    certification_date = models.DateField(default=date.today)
    email1 = models.EmailField(max_length=254, blank=False) 
    
    issue_by = models.CharField(max_length = 50) 

    unique_id1 = models.UUIDField(primary_key=True,editable=False) 