from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Car(models.Model):
    color = models.CharField(max_length=30)
    doors = models.IntegerField(default=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity_engine = models.IntegerField()
    date_fabricated = models.DateField()
    mechanical_revision = models.BooleanField(default=True)
    plate = models.CharField(
        max_length=6
    )

    def __str__(self):
        return self.plate

    def get_plate(self):
        return self.plate


class Parking(models.Model):
    name = models.CharField(max_length=150)
    description_marketing = models.TextField()
    cars = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
