# example/urls.py
from django.urls import path,include,re_path
from example.views import login_view,student_view,teacher_view,sign_view
app_name='example'
urlpatterns = [
    path('login/', login_view,name='login'),
    path('',sign_view,name='signin'),
    path('student/',student_view,name='student_view'),
    path('teacher/',teacher_view,name='teacher_view'),
]
