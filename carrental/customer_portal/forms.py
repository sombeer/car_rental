from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    mobileNo = forms.IntegerField()
    aadharCard = forms.IntegerField()
    drivingLicense = forms.IntegerField()

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'password1', 'password2', 'drivingLicense', 'aadharCard')