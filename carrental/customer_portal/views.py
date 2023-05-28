from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse
from .forms import UserRegistrationForm

def index(request):
    return render(request,'index.html')
    

#register user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('customer_portal:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'car_rental/register.html', {'form': form})

#user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('/')
        else:
            # Invalid login credentials
            return render(request, 'car_rental/login.html', {'error': 'Invalid username or password.'})
    else:
        # Display the login form
        return render(request, 'car_rental/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('/')
    
