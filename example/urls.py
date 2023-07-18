# example/urls.py
from django.urls import path,include
from . import views  

urlpatterns = [
    path('my-view/', include('my_view')),
    path('students/', include('student_list')),
    path('teachers/', include('teacher_list')),
]
