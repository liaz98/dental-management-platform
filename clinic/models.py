from django.db import models

# Create your models here.


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name
