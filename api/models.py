from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')


class Diagnose(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    doctor = models.ForeignKey(User, related_name='patients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    diagnoses = models.ManyToManyField(Diagnose)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
