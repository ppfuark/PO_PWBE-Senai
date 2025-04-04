from django.db import models

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=10)
    descricao = models.TextField()
    status = models.BooleanField()