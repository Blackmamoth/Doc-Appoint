from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import datetime


def validate_phone(phone):
    if not int(phone):
        raise ValidationError('Phone number must contain only digits')
        

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[validate_phone])
    clinic_address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    checkup_for = models.CharField(max_length=100)

    def __str__(self):
        return f'Appointment of {self.patient.username} with {self.doctor.name} for {self.checkup_for}'
    