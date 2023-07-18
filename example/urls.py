# example/urls.py
from django.urls import path
from . import views  

urlpatterns = [
    path('my-view/', views.my_view),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
]
