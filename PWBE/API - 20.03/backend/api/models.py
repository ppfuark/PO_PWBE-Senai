from django.db import models

class Event(models.Model):
    name = models.TextField()
    description = models.TextField()
    day = models.DateField()  
    time = models.TimeField()
    local = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.day}"
