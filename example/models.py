from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
  is_student = models.BooleanField(default=True)
  username=models.CharField(max_length=100)
  password=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)

class Teacher(AbstractUser):
  is_student = models.BooleanField(default=False)
  username=models.CharField(max_length=100)
  password=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)

