from .views import *
from django.urls import path


urlpatterns = [
    path('aboutus/',about_us),
    path('contactus/',contact_us),

]