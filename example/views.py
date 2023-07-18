# example/views.py
from django.shortcuts import render, redirect
from example.models import Student, Teacher
from django.contrib.auth import get_user_model

def student_list(request):
    students = Student.objects.all()
    return render(request, 'Template/student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Add additional fields as needed
        User = get_user_model()
        user = User.objects.create_user(username=username, password=password)
        # Save additional fields if necessary
        return redirect('home')  # Replace 'home' with your desired URL
    return render(request, 'index.html')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'Templates/teacher_list.html', {'teachers': teachers})

def create_employee(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Add additional fields as needed
        User = get_user_model()
        user = User.objects.create_user(username=username, password=password)
        # Save additional fields if necessary
        return redirect('home')  # Replace 'home' with your desired URL
    return render(request, 'create_employee.html')

def my_view(request):
    return render(request, 'Templates/index.html')
