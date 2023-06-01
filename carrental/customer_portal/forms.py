from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    mobileNo = forms.IntegerField()
    drivingLicenseNo = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email', 'password1', 'password2', 'drivingLicenseNo','mobileNo')

