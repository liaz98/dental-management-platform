from django.db import models


# Create your models here.
from clinic.models import Clinic


class Procedure(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    NPI = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    specialties = models.ManyToManyField(Procedure)  # predefined list of specialties
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    clinics = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="clinic")

    def __str__(self):
        return self.name
