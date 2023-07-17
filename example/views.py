# example/views.py
from django.shortcuts import render

def my_view(request):
    return render(request, 'Templates/index.html')

def my_data(request):
    data=Student.objects.all()
    return render(request,'Templates/student-login.html')
