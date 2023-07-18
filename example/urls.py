# example/urls.py
from django.urls import path,include
from example.views import my_view,student_list,teacher_list  

urlpatterns = [
    path('', views.my_view),
    path('', views.student_list),
    path('', views.teacher_list),
]
