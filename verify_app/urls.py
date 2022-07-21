from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',verify_key_view),
    path('key/<str:verify_key>/',certificate_view)
]