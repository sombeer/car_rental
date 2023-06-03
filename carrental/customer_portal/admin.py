from django.contrib import admin
from .models import Customer,Vehicle,RentalBooking,RentalTransaction,Location
from django.utils.html import format_html
from .models import Vehicle
from django import forms

#change admin name,title
admin.site.site_header = 'HILLDRIVE'
admin.site.site_title = 'HILLDRIVE'
admin.site.index_title = 'Welcome to HILLDRIVE Admin'
admin.site.site_header_icon = 'path_to_your_icon.png'

#register model and display list in admin panel

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","username","email","phone_number","address","is_active","admin_drivingLicenseNo")
    search_fields=("name","email")
    fields = ("name","username","email","password","phone_number","address","is_active","drivingLicenseNo")
    readonly_fields = ("admin_drivingLicenseNo",)

    def admin_drivingLicenseNo(self, obj):
        return format_html('<img src="{}" style="max-width: 150px; max-height: 150px;" />', obj.drivingLicenseNo.url)
    admin_drivingLicenseNo.short_description = 'Driving License Preview'


class VehicleAdminForm(forms.ModelForm):
    image = forms.ImageField(widget=admin.widgets.AdminFileWidget, required=False)

    class Meta:
        model = Vehicle
        fields = '__all__'    
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model","name","color","year","fuel_type","transmission_type","rental_price","admin_image")
    list_filter=("model",)
    readonly_fields = ("admin_image",)
    def admin_image(self, obj):
        return format_html('<img src="{}" style="max-width: 150px; max-height: 150px;" />', obj.image.url)
    admin_image.short_description = 'Image Preview'



@admin.register(RentalBooking)
class RentalBookingAdmin(admin.ModelAdmin):
    list_display = ["user","vehicle","return_location","return_location","pickup_date","return_date","rental_status"]


@admin.register(RentalTransaction)
class RentalTransactionAdmin(admin.ModelAdmin):
    list_display = ["booking","payment_method","total_amount","transaction_status","payment_date"]


@admin.register(Location)
class RLocationAdmin(admin.ModelAdmin):
    list_display = ("location_name","address","contact_information","operating_hours")

