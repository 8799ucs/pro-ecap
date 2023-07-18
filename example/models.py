from django.contrib.auth.models import AbstractUser
from django.db import models


class Student(AbstractUser):
  username=models.CharField(max_length=100)
  password=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)

class Student(AbstractUser):
  username=models.CharField(max_length=100)
  password=models.CharField(max_length=100)
  name=models.CharField(max_length=100)
  phone=models.CharField(max_length=100)

