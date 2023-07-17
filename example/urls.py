# example/urls.py
from django.urls import path, include
from django.contrib import admin
from example.views import my_view, my_data

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', my_view),
    path('Templates/student-login/',my_data),
]
