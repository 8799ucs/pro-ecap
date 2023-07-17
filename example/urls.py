# example/urls.py
from django.urls import path
from example.views import my_view, create_user, login_user

urlpatterns = [
    path('', my_view),
    path('',create_user),
    path('login/',login_user),
]
