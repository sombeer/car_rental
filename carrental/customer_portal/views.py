from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .forms import UserRegistrationForm
from .models import Customer
import random
from django.core.mail import send_mail




def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')

def shop(request):
    return render(request,'shop.html')



#register user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Customer.objects.filter(email=email).exists():
                return render(request, 'car_rental/register.html', {'form': form, 'error_message': 'Email already exists.'})
            form.save()
            return redirect(reverse('customer_portal:login') )     
    else:
        form = UserRegistrationForm()

    return render(request, 'car_rental/register.html', {'form': form})


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
    
