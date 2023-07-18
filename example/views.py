# example/views.py
from django.shortcuts import render
from example.models import Student, Teacher

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student-login.html', {'students': students})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher-login.html', {'teachers': teachers})

def my_view(request):
    return render(request, 'Templates/index.html')
