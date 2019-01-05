from datetime import datetime
from django.utils import timezone
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
    join_date = models.DateField(blank=True, default=timezone.now)
    date_of_birth = models.DateField(blank=True)
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
    sec = models.OneToOneField(CustomUser, on_delete=models.CASCADE, help_text="Enter the SEC of this outlet")
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


class Visit(models.Model):
    foe = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)


class Attendance(models.Model):
    sec = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="Enter the sec")
    date = models.DateField(default=timezone.now)
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, help_text="Enter the outlet")
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    picture = models.ImageField(help_text="Insert the picture here")


class Leave(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, help_text="Enter the outlet name")
    date = models.DateField(default=timezone.now)
    LEAVE_TYPE = (
        (1, "half day"),
        (2, "full day"),
    )
    leave_type = models.IntegerField(choices=LEAVE_TYPE, default=1)
    remark = models.CharField(max_length=300, help_text="Enter the reason of the leave")
    authorized_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="Enter who authorized this leave")


class Sales(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, help_text="Enter the customer name")
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE, help_text="Enter the outlet name")
    date_time = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(ProductVariation, on_delete=models.CASCADE, help_text="Enter the product name")
    amount = models.IntegerField(help_text="Price of the sold product")
    # two different mobiles in one sale?
    # I assume one product can be sold in a sale. otherwise i have to add a field "quantity"


class Stock(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    product_total_price = models.IntegerField()
    stock_update_date = models.DateTimeField()
    # if sales and target are here why we need stock table?


class Target(models.Model):
    outlet = models.ForeignKey(Outlet, on_delete=models.CASCADE)
    MONTH_CHOICE = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )
    month = models.IntegerField(choices=MONTH_CHOICE, default=1)
    productVariation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
    quantity = models.IntegerField(help_text="Enter the quantity of this product")
    total_amount = models.IntegerField()









