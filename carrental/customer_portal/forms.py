from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class UserRegistrationForm(UserCreationForm):
    #mobileNo = forms.IntegerField()
   # drivingLicenseNo = forms.ImageField()
 

    class Meta:
        model = Customer
        fields = ('name','username','email', 'password1', 'password2', 'drivingLicenseNo','phone_number')

        