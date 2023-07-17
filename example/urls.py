# example/urls.py
from django.urls import path
from example.views import my_view, my_data, login_user

urlpatterns = [
    path('', my_view),
    path('login/',login_user),
]
