from .views import *
from django.urls import path
from django.contrib.auth.decorators import login_required


# path('create_click/',create_click),
# path('certificate_page/',student_detail_html),
# path('finish/<str:user1>/',finish_view,name="finish_view"),


urlpatterns = [
    path('dashboard/',dashboard),
    path('create_certificate/',student_detail_html),
    path('finish/<str:user1>/',finish_view),


]