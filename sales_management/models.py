from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, help_text='Enter the first name')
    last_name = models.CharField(max_length=100, help_text='Enter the last name')
    GENDER_CHOICE = (
        (1, "Male"),
        (2, "Female"),
    )
    gender = models.IntegerField(choices=GENDER_CHOICE, default=1)
    phone = models.IntegerField(blank=True, default=123)
    join_date = models.DateField(blank=True, default=datetime.now())
    date_of_birth = models.DateField(blank=True, default=datetime.now())
    address = models.CharField(max_length=300)
    picture = models.ImageField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=100, help_text='Enter product name')


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, help_text="Enter the color")
    active = models.BooleanField(default=True)


class Region(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the region name")


class Area(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the area name")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class District(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the district name")
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Territory(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the territory name")
    district = models.ForeignKey(District, on_delete=models.CASCADE)


class Outlet(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the Outlet name")
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    outlet_type = models.CharField(max_length=100, help_text="Enter the outlet type name")
    address = models.CharField(max_length=300, help_text="Enter the address of the outlet")
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

    STATUS_CHOICES = (
        (1, "Saturday"),
        (2, "Sunday"),
        (3, "Monday"),
        (4, "Tuesday"),
        (5, "Wednesday"),
        (6, "Thursday"),
        (7, "Friday"),

    )

    day_off = models.IntegerField(choices=STATUS_CHOICES, default=7, help_text="Enter day off (Firday is default)")
    active = models.BooleanField(default=True)






