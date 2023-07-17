# example/urls.py
from django.urls import path, include
from django.contrib import admin
from example.views import my_view, my_data, login_user

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', my_view),
    path('login/',login_user),
]
