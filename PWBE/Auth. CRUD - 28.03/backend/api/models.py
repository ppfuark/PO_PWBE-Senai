from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True)
    pet_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.username