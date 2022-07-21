from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',regsiter_view),
    path('registering/',register)

]