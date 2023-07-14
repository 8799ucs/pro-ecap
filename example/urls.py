# example/urls.py
from django.urls import path
from example.views import my_view

urlpatterns = [
    path('', my_view)
]
