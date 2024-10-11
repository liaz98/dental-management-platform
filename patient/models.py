from django.db import models

# Create your models here.
from clinic.models import Clinic
from doctor.models import Doctor, Procedure


class Patient(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    ssn_last4 = models.CharField(max_length=4)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.name


class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    visit_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)
    procedures_done = models.ManyToManyField(Procedure)
    doctor_notes = models.TextField()

    def __str__(self):
        return f"Visit for {self.patient.name} on {self.visit_date}"


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    procedure = models.ForeignKey(Procedure, on_delete=models.SET_NULL, null=True)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment_date}"