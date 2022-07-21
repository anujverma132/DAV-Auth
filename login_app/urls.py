from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login_page/',login_page),
    path('login_page/submit/',login1),
    path('logout/',logout1),
]