from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission
from django.core.validators import MaxValueValidator
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    mobileNo = models.IntegerField(default=0,validators=[MaxValueValidator(9999999999)])
    drivingLicenseNo = models.ImageField( upload_to='driving_license', height_field=None,width_field=None,null=False,blank=False)
    email_code=models.IntegerField(default=0,blank=False,null=False)
    is_active = models.BooleanField(default=0,null=False)

    REQUIRED_FIELDS = ['first_name', 'last_name']
   
    

     # Specify unique related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customer_users'  # Unique related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customer_users'  # Unique related_name
    )

    def __str__(self):
        return self.username

class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    rental_price = models.DecimalField(max_digits=8, decimal_places=2)

class RentalBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    return_location = models.CharField(max_length=255)
    pickup_date = models.DateField()
    return_date = models.DateField()
    pickup_time = models.DateField()
    return_time = models.DateField()
    rental_status = models.CharField(max_length=50)

class RentalTransaction(models.Model):
    booking = models.ForeignKey(RentalBooking, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_status = models.CharField(max_length=50)
    payment_date = models.DateField()

class Location(models.Model):
    location_name = models.CharField(max_length=255)
    address = models.TextField()
    contact_information = models.CharField(max_length=255)
    operating_hours = models.CharField(max_length=255)


