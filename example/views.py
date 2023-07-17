# example/views.py
from django.contrib.auth.models import Studentuser
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect

def login_user(request):
    if(request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authentication(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Templates/student-login.html')
        else:
            return render(request,'index.html',{'error':'Invalid username or password'})
return render(request,'index.html')

def my_view(request):
    return render(request, 'Templates/index.html')

def create_stu(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        phone=request.POST['phone']
        stuser=Studentuser.objects.create_user(username=username, password=password, name=name, phone=phone)
        stuser.save()
        return redirect('student-login.html')

def my_data(request):
    data=Student.objects.all()
    return render(request,'Templates/student-login.html')
