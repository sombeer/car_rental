from django.contrib import admin
from .models import User,Vehicle,RentalBooking,RentalTransaction,Location

# Register your models here.
admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(RentalBooking)
admin.site.register(RentalTransaction)
admin.site.register(Location)
