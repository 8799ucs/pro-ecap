# example/urls.py
from django.urls import path,include
from . import views  

urlpatterns = [
    path('my-view/', views.my_view),
    path('students/', views.student_list),
    path('teachers/', views.teacher_list),
]
