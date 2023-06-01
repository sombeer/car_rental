from django.urls import include, path
from . import views
app_name='customer_portal'

urlpatterns = [
       path('',views.index,name='home'),
       path('register/', views.register, name='register'),
       path('otp_verification/<str:user_email>/',views.otp_verification,name='otp'),
       path('login/', views.login_view, name='login'),
       path('logout/',views.logout_user,name='logout'),
  
       ]
