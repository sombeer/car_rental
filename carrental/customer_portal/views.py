from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import UserRegistrationForm
from .models import Customer,Vehicle,RentalBooking
import random
from django.core.mail import send_mail
from django.shortcuts import render
from datetime import datetime, timedelta
from urllib.parse import unquote
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'index.html',{'cars':cars})

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')

from urllib.parse import unquote

def cars(request):
    # Retrieve the pickup date and return date from the search form
    #unquote() is used to decode the URL-encoded characters in the date strings. 
    pickup_date_str = unquote(request.GET.get('pickup_date'))
    return_date_str = unquote(request.GET.get('return_date'))
    
    # Convert the date strings to datetime objects
    #The date format in strptime() is modified to ' %B %d, %Y' to match the format in the URL parameters.
    pickup_date = datetime.strptime(pickup_date_str, ' %B %d, %Y').date()
    return_date = datetime.strptime(return_date_str, ' %B %d, %Y').date()
    
    # Query the rental booking model for bookings matching the pickup and return dates
    bookings = RentalBooking.objects.filter(pickup_date=pickup_date, return_date=return_date)
    
    # Fetch all cars from the car model
    cars = Vehicle.objects.all()
    
    # Create a dictionary to store the car status (booked or available)
    car_status = {}
    
    # Iterate over each car and check if it has a booking for the specified dates
    for car in cars:
        if bookings.filter(vehicle=car).exists():
            car_status[car.id] = 'Booked'
        else:
            car_status[car.id] = 'Available'
    
    # Render the HTML template with the car data, status, pickup_date, and return_date
    return render(request, 'cars.html', {'cars': cars, 'car_status': car_status, 'pickup_date': pickup_date, 'return_date': return_date})



def booking(request):
    id = request.GET.get('car_id')
    pickup_date_str = request.GET.get('pickup_date')
    return_date_str = request.GET.get('return_date')
    
    # Convert pickup_date_str and return_date_str to datetime objects
    #strip() to remove any leading or trailing whitespace from the date strings before converting them to datetime objects.
    pickup_date = datetime.strptime(pickup_date_str, ' %B %d, %Y').date()
    return_date = datetime.strptime(return_date_str, ' %B %d, %Y').date()    
    hours = (return_date - pickup_date).total_seconds() // 3600

    car = get_object_or_404(Vehicle, id=id)
    car.hours = hours

    return render(request, 'car-detail.html', {'car': car, 'pickup_date': pickup_date, 'return_date': return_date})

@login_required
def user_booking_process(request):
    car_id=request.GET.get('car_id')
    current_user = request.user
    print (current_user.id)
    car = Vehicle.objects.filter(id=id)
    return render(request, 'car-detail.html',{'car':car})


#register user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Customer.objects.filter(email=email).exists():
                return render(request, 'register.html', {'form': form, 'error_message': 'Email already exists.'})
            form.save()
            return redirect(reverse('customer_portal:login') )     
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


#user login
def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        print(username , password , auth_user)
        if auth_user is not None and isinstance(auth_user, Customer):
            if auth_user.is_active:
                login(request, auth_user)
                # Redirect to a success page
                return redirect('/')
            else:

                #send email to verify email
                 # Generate OTP
                otp = str(random.randint(100000, 999999))

               # Save OTP to the database
                
                auth_user.email_code = otp
                auth_user.save()
            
                # Send OTP to email
                send_mail(
                    'OTP Verification',
                    f'Your OTP: {otp}',
                    'hilldrive.in@gmail.com',
                    [auth_user.email],
                    fail_silently=False
                )
               # return redirect(reverse('customer_portal:otp' + f'?email={user_email}'))
                return redirect(reverse('customer_portal:otp', kwargs={'user_email': auth_user.email}))
        else:
            # Invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid username or password.'})
    else:
        # Display the login form
        return render(request, 'login.html')
    
#generate otp for registerion user email

def otp_verification(request,user_email):

    if request.method == 'POST':
        otp_verification = int(request.POST.get('otp'))
        user = get_object_or_404(Customer, email=user_email)
        print(user)
        # Verify the entered OTP => user = get_object_or_404(User, email=user_email, email_code=otp_verification)
        if user.email_code == otp_verification:
            user.is_active = True
            user.save()
            return render(request, 'index.html')
        else:
            error_message = "Invalid OTP. Please try again."
            return render(request, 'car_rental/otp.html', {'error_message': error_message})
    else:
        return render(request, 'car_rental/otp.html')
    
def logout_user(request):
    logout(request)
    return redirect('/')
    
