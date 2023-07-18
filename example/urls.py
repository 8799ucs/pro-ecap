# example/urls.py
from django.urls import path
from example.views import my_view, student_list,teacher_list  

urlpatterns = [
    path('', my_view),
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
]
