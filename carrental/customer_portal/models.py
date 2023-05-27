from django.db import models
from django.contrib.auth.models import AbstractUser , Group , Permission

# Create your models here.

class User(AbstractUser):
    mobileNo = models.IntegerField(default=0)
    aadharCardNo = models.IntegerField(default=0)
    drivingLicenseNo = models.IntegerField(default=0)

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


