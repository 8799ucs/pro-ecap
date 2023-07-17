# example/views.py
from django.shortcuts import render
from .models import Student

def my_view(request):
    return render(request, 'templates/index.html')

def my_data(request):
    data=Student.objects.all()
    return render(request,'templates/student-login.html')
