# example/views.py
import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from example.models import Student, Teacher
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.conf import settings 
from . import *
import os
def view(request):
    return render(request,'templates/index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        dbase = sqlite3.connect(os.path.join(settings.BASE_DIR, 'bdata.db'))
        cursor = dbase.cursor()
        cursor.execute("SELECT * FROM Student WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        if(user_data):
                db_username = user_data[0]
                db_password = user_data[1]
                name = user_data[2]
                phone = user_data[3]
                if password == db_password:
                    return student_view(request)
                else:
                    return render(request, 'templates/index.html')
        else:
            return render(request, 'templates/index.html')

    else:
        return render(request, 'templates/index.html')
def sign_view(request):
    if request.method == 'POST':
        username = request.POST.get('username1','')
        password = request.POST.get('password1','')
        dbase = sqlite3.connect(os.path.join(settings.BASE_DIR, 'bdata.db'))
        cursor = dbase.cursor()
        cursor.execute("SELECT * FROM Teacher WHERE username = ?", (username,))
        user_data = cursor.fetchone()
        if(user_data):
                db_username = user_data[0]
                db_password = user_data[1]
                name = user_data[2]
                phone = user_data[3]
                if password == db_password:
                    return teacher_view(request)
                else:
                    return render(request,'templates/index.html')
        else:
            return login_view(request)

    else:
        return render(request, 'templates/index.html')
def student_view(request):
    username = request.POST['username']
    dbase = sqlite3.connect(os.path.join(settings.BASE_DIR, 'bdata.db'))
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM Student WHERE username = ?", (username,))
    students = cursor.fetchone()
    s=students[2]
    return render(request,'templates/student_list.html',{'data': s})
def teacher_view(request):
    username = request.POST['username1']
    dbase = sqlite3.connect(os.path.join(settings.BASE_DIR, 'tdata.db'))
    cursor = dbase.cursor()
    cursor.execute("SELECT * FROM Teacher WHERE username = ?", (username,))
    teachers= cursor.fetchone()
    t=teachers[2]
    return render(request,'templates/teacher_list.html',{'data': t})
