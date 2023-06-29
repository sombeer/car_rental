from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='customer_portal'
urlpatterns = [
    # Other URL patterns
    
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
   
    path('cars/', views.cars, name='cars'),
    path('booking/', views.booking, name='booking'),
    path('car-booking/', views.car_booking_process, name='carbooking'),
    path('payment-success/', views.payment_success, name='paymentsuccess'),
    path('user-booking/', views.userBooking, name='userbooking'),
   
    path('profile/', views.userprofile, name='userprofile'),
    path('register/', views.register, name='register'),
    path('otp_verification/<str:user_email>/', views.otp_verification, name='otp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       