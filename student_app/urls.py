from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user_certificate/',issued_certificate_list),

]