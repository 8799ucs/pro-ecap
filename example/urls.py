# example/urls.py
from django.urls import path
from example.views import my_view

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', my_view)
]
