from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
# Create your models here.

class Customer(AbstractUser):
    USERNAME_FIELD = 'username'
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    email_code=models.IntegerField(default=0,blank=False,null=False)
    is_active = models.BooleanField(default=0,null=False)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    drivingLicenseNo = models.ImageField( upload_to='driving_license',null=False,blank=False)
    

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customer_groups'  # Add a unique related_name argument
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customer_user_permissions'  # Add a unique related_name argument
    )

    
class Vehicle(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    model = models.CharField(max_length=255,blank=True)
    year = models.PositiveIntegerField(blank=True,null=True)
    color = models.CharField(max_length=50,blank=True)
    fuel_type = models.CharField(max_length=50,null=False,blank=False)
    fuel_capacity = models.PositiveIntegerField(null=False,blank=False,default=0)
    transmission_type = models.CharField(max_length=50 ,null=False)
    rental_price = models.DecimalField(max_digits=8, decimal_places=2,null=False,blank=False)
    base_package_free_km = models.PositiveIntegerField( null=False,blank=False,default=0)
    medium_package = models.DecimalField(max_digits=8, decimal_places=2,null=False,blank=False,default=0)
    medium_package_free_km = models.PositiveIntegerField( null=False,blank=False,default=0)
    unlimited_package = models.DecimalField(max_digits=8, decimal_places=2,null=False,blank=False,default=0)
    excess_km_charge=models.PositiveIntegerField(null=False,blank=False,default=0)
    image = models.ImageField(upload_to='car_images' ,null=False,blank=False)

   
  

class RentalBooking(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    return_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    return_date = models.DateField()
    is_booked = models.BooleanField(default=0,null=False)
    
    def __str__(self):
        return str(self.pk) 

class RentalTransaction(models.Model):
    booking = models.ForeignKey(RentalBooking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_status = models.CharField(max_length=50)
    payment_date = models.DateField(auto_now=True)
    razor_pay_order_id = models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id = models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature = models.CharField(max_length=100,null=True,blank=True)
    is_paid = models.BooleanField(default=0,null=False)
    # is_payment_verify=models.BooleanField(default=0,null=False)


    def __str__(self):
        return str(self.pk) 

class Location(models.Model):
    location_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_information = models.CharField(max_length=255)
    operating_hours = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name

