# example/views.py
from django.shortcuts import render, redirect
from example.models import Student, Teacher

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_student = bool(int(request.POST.get('is_student', 0)))

        # Create the appropriate user instance based on the is_student parameter
        if is_student:
            user = Student.objects.create_user(username=username)
        else:
            user = Teacher.objects.create_user(username=username)

        # Set the user's password
        user.set_password(password)
        user.save()

        return redirect('login')  # Redirect to the login page after user creation

    return render(request, 'create_user.html')



def my_view(request):
    return render(request, 'Templates/index.html')
