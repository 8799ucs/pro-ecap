# example/urls.py
from django.urls import path
from example.views import my_view,my_data

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', my_view),
    path('student-login/',my_data),
]
