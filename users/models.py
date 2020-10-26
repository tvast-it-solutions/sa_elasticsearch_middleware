from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_CHOICES = (
        ('Admin', 'admin'),
        ('Analyst', 'analyst'),
    )
    userType = models.CharField(choices=USER_CHOICES,max_length=50)

    def __str__(self):
        return f"{self.email} - {self.username} - {self.userType}"