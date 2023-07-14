# example/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('myurl/', views.my_view, name='my-view'),
]
