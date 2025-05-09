from django.db import models

class Teacher(models.Model):
    ni = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    born_date = models.DateField()
    hire_date = models.DateField()
    assigned_subjects = models.ManyToManyField('Subject',blank=True, related_name="assigned_teachers")

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    workload = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.name

class RoomReservation(models.Model):
    PERIOD_CHOICES = [
        ('M', 'morning '),
        ('A', 'afternoon'),
        ('N', 'night'),
    ]

    start_date = models.DateField()
    end_date = models.DateField()
    period = models.CharField(max_length=1, choices=PERIOD_CHOICES)
    room = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="reservations")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="reservations")

    def __str__(self):
        return f"{self.room} - ({self.start_date} | {self.end_date})"
