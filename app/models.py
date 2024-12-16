# app/models.py
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

class Unit(models.Model):
    unit_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.unit_name

class Stock(models.Model):
    stock_name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.stock_name} ({self.unit})"

class Customer(models.Model):
    GROUP_CHOICES = [
        ('Active', 'Active'),
        ('One Time', 'One Time')
    ]

    customer_name = models.CharField(max_length=100)
    mobile_no = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)]
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    group_type = models.CharField(max_length=8, choices=GROUP_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    follow_up_customer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.mobile_no}"

class AdvanceBooking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateField()
    due_date = models.DateField()
    need = models.CharField(max_length=255)
    total_load = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.customer} on {self.booking_date}"

class Demand(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    total_load = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Demand: {self.customer} - {self.stock}"

class Supply(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    total_load = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Supply: {self.customer} - {self.stock}"