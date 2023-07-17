# example/views.py
from examples.models import Student
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def create_user(request):
    # Get a reference to the Firestore database
    db = firestore.client()

    # Perform database operations
    doc_ref = db.collection('users').document('new_user')
    doc_ref.set({
        'username': '21241A6737',
        'password': '21241A6737',
        'name':'Nagula Navya sri',
        'phone':'7893762846',
    })


def login_user(request):
    if request.method=='POST' :
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Templates/student-login.html')
        else:
            return render(request,'Templates/index.html',{'error':'Invalid username or password'})
    else :
        return render(request,'Templates/index.html')

def my_view(request):
    return render(request, 'Templates/index.html')
