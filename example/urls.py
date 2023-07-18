# example/urls.py
from django.urls import path,include
from . import views  

urlpatterns = [
    path('', views.my_view),
    path('', views.student_list),
    path('', views.teacher_list),
]
