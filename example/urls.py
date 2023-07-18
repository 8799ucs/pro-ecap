# example/urls.py
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.my_view),
    path('', views.student_list, name='student_list'),
    path('', views.teacher_list, name='teacher_list'),
]
