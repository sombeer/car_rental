from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import UserRegistrationForm
from .models import Customer,Vehicle,RentalBooking,RentalTransaction
import random
from django.core.mail import send_mail
from django.shortcuts import render
from datetime import datetime,timedelta
from urllib.parse import unquote
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from django.conf import settings
import razorpay
from django.http import HttpResponse
from decimal import Decimal
from django.contrib import messages
from django.contrib.sessions.models import Session
import os


def index(request):
    cars = Vehicle.objects.all()
    return render(request,'index.html',{'cars':cars})

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')

def cars(request):
    pickup_date_str = unquote(request.GET.get('pickup_date'))
    return_date_str = unquote(request.GET.get('dropoff_date'))
    
  
    
    pickup_date = datetime.strptime(pickup_date_str, '%Y-%m-%d').date()
    return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()
    
    
    
    bookings = RentalBooking.objects.filter(pickup_date=pickup_date, return_date=return_date)
    
    cars = Vehicle.objects.all()
    
    car_status = {}
    
    for car in cars:
        if bookings.filter(vehicle=car).exists():
            car_status[car.id] = 'Booked'
        else:
            car_status[car.id] = 'Available'
    
    
    
    return render(request, 'cars.html', {'cars': cars, 'car_status': car_status, 'pickup_date': pickup_date, 'return_date': return_date})


def booking(request):
    id = request.GET.get('car_id')
    pickup_date_str = request.GET.get('pickup_date')
    return_date_str = request.GET.get('return_date')

    pickup_date = datetime.strptime(pickup_date_str, '%B %d, %Y').date()
    return_date = datetime.strptime(return_date_str, '%B %d, %Y').date()

    hours = (return_date - pickup_date).total_seconds() // 3600


    car = get_object_or_404(Vehicle, id=id)
    rental_price = Decimal(str(car.rental_price))
    hours_rent = (rental_price / Decimal('12')) * Decimal(str(hours))

    car.hours_rent =hours_rent

    car.hours = hours

    return render(request, 'car-detail.html', {'car': car, 'pickup_date': pickup_date, 'return_date': return_date})


@login_required
@user_passes_test(lambda u: not u.is_staff, login_url='/login/')
def car_booking_process(request):
    hours_rent = 0 
    if request.method == 'GET':
        car_id = request.GET.get('car_id')
        car = get_object_or_404(Vehicle, id=car_id)
        
        name = request.GET.get('name')
        model = request.GET.get('model')
    
        fuel_type = request.GET.get('fuel_type')
        hours_rent = Decimal(request.GET.get('hours_rent'))

        pickup_date_str = request.GET.get('pickup_date')
        return_date_str = request.GET.get('drop-date')
        
        
        # Convert date strings to datetime objects
        pickup_date = datetime.strptime(pickup_date_str, "%B %d, %Y")
        return_date = datetime.strptime(return_date_str, "%B %d, %Y")

        check_availablity = RentalBooking.objects.filter(pickup_date=pickup_date, return_date=return_date,vehicle=car)
        
    
        client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
        data = {
            "amount": int(hours_rent * 100),  # Amount in paise (e.g., 50000 paise = 500 INR)
            "currency": "INR",
            "receipt": f"order_rcptid_{car_id}"  # Use a unique identifier for each receipt
        }
        payment = client.order.create(data=data)
      
        order_id=payment['id']

        # if check_availablity.exists():
        #     check_user_same=RentalBooking.objects.filter(pickup_date=pickup_date, return_date=return_date,vehicle=car,user=request.user)
        #     if check_user_same.exists():
        #         check_user_paid = RentalTransaction.objects.filter(booking_id=check_user_same.id,is_paid=True)
                
        #         if check_user_paid.exists():
        #             messages.error(request, 'call to customer care and verify your payment ! ')
        #             return redirect('customer_portal:home')
        #         messages.error(request, 'call to customer care your payment is not done yet ! ')
        #         return redirect('customer_portal:home')

        #     messages.error(request, 'something went wrong ! ')
        #     return redirect('customer_portal:home')
        
        rental_booking = RentalBooking.objects.create(
        user=  request.user ,
        vehicle=car,
        pickup_location='Udaipur',
        return_location='Udaipur',
        pickup_date=pickup_date,
        return_date=return_date,
        is_booked=True
        )
        if order_id:
           
            # Save payment details in the rental transaction
            rental_transaction = RentalTransaction.objects.create(
                booking=rental_booking,
                payment_method="Razorpay",  # Update with the actual payment method
                total_amount=hours_rent,
                transaction_status="Success",  # Update with the actual transaction status
                
                razor_pay_order_id=order_id
            )
            
            messages.success(request, 'Booking processed successfully,Please make the payment')
        else:
            # Payment failed or not completed
            messages.error(request, 'Payment failed. Please try again.')
            
        context = {
            "car_id": car_id,
            "name": name,
            "model": model,
            "fuel_type": fuel_type,
            "hours_rent": hours_rent,
            "pickup_date_str": pickup_date.strftime("%B %d, %Y"),
            "return_date_str": return_date.strftime("%B %d, %Y"),
            "payment":payment,
            "image":car.image,

        }
        return render(request, 'Car_booked_sucessfully.html', context=context)       

@login_required
@user_passes_test(lambda u: not u.is_staff, login_url='/login/')
def payment_success(request):
    razorpay_payment_id = request.GET.get('razorpay_payment_id')
    razorpay_order_id = request.GET.get('razorpay_order_id')
    razorpay_signature = request.GET.get('razorpay_signature')
    try:
        print("razorpay_payment_id")
        rental_transaction = RentalTransaction.objects.get( razor_pay_order_id=razorpay_order_id)
        rental_transaction.is_paid = True
        razor_pay_payment_id=razorpay_payment_id
        razor_pay_payment_signature=razorpay_signature
        rental_transaction.save()
       
    except RentalTransaction.DoesNotExist:
        # Handle the case where the RentalTransaction object does not exist
        # For example, display an error message or redirect the user to an error page
        # You can also log the error for debugging purposes
        messages.error(request, 'call to customer care your payment is not done yet ! ')
        return redirect('customer_portal:userbooking')
    
    messages.success(request, 'booking successfull')
    return redirect('customer_portal:userbooking')

@login_required
@user_passes_test(lambda u: not u.is_staff, login_url='/login/')
def userBooking(request):
    user = request.user
    previous_booking = RentalBooking.objects.filter(user=user)
    
    current_booking = RentalBooking.objects.filter(user=user).latest('id')
    current_transaction = RentalTransaction.objects.get(booking=current_booking)
    previous_transactions = []
    for booking in previous_booking:
        try:
            transaction = RentalTransaction.objects.get(booking=booking)
            previous_transactions.append(transaction)
        except RentalTransaction.DoesNotExist:
            # Handle the case where a transaction does not exist for the booking
            # You can either skip this booking or add a placeholder object to the list
            # For example:
            # placeholder_transaction = RentalTransaction()
            # previous_transactions.append(placeholder_transaction)
            pass
    
    context = {
        'previous_booking': previous_booking,
        'previous_transactions': previous_transactions,
        'current_booking':current_booking,
        'current_transaction':current_transaction

    }
    return render(request, 'userbookings.html', context)



@login_required
@user_passes_test(lambda u: not u.is_staff, login_url='/login/')
def userprofile(request):
    user = Customer.objects.get(username=request.user)
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(user.drivingLicenseNo) > 0:
                os.remove(user.drivingLicenseNo.path)
            user.drivingLicenseNo  = request.FILES['image']
        user.name         = request.POST.get('name')
        user.phone_number = request.POST.get('phone_number')
        user.address      = request.POST.get('address')
        user.username     = request.POST.get('username')
        user.email        = request.POST.get('email')
        password          = request.POST.get('password')
        user.set_password(password)
        user.save()
        messages.success(request,'category update successfully')
        return redirect('/profile')
    return render (request,'profile.html',{'user':user})

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
                logout(request)
                login(request, auth_user)
                # Redirect to a success page
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
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

def otp_verification(request, user_email):
    if request.method == 'POST':
        entered_otp = int(request.POST.get('otp'))
        user = get_object_or_404(Customer, email=user_email)
        print(entered_otp)
        if entered_otp == user.email_code:
            user.is_active = True
            user.save()
            messages.success(request,"your email is verified,now you can login your account")
            return render(request, 'index.html')
        else:
            error_message = "Invalid OTP. Please try again."
            return render(request, 'otp.html', {'error_message': error_message})
    else:
        return render(request, 'otp.html')

    
def logout_user(request):
    logout(request)
    return redirect('/')

