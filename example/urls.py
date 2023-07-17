# example/urls.py
from django.urls import path, include
from django.contrib import admin
from accounts.views import login_user
from example.views import my_view, my_data

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', my_view),
    path('login/',login_user),
    path('Templates/student-login/',my_data),
]
