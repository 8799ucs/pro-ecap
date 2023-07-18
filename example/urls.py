# example/urls.py
from django.urls import path,include
from example.views import my_view,student_list,teacher_list  
app_name='example'
urlpatterns = [
    path('', my_view),
    path('', student_list),
    path('', teacher_list),
]
