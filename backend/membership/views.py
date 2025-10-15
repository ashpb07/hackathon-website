from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html')

def singin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        if username and pass1:
            user = authenticate(username=username, password=pass1)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('member')  
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Please fill in all fields")
        
        return redirect('home')
    
    return redirect('home')

def singup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        fname = request.POST.get('fname', '')
        email = request.POST.get('email', '')
        
        # Validation
        if not all([username, pass1, pass2]):
            messages.error(request, "Please fill in all required fields")
            return redirect('home')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "Email already exists")
            return redirect('home')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('home')    

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('home')
            
        # Create user
        try:
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.first_name = fname
            myuser.save()
            
            messages.success(request, "Signup successful! Please login.")
            return redirect('home')
            
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return redirect('home')
    
    return redirect('home')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def member(request):
    if request.user.is_authenticated:
        return HttpResponse(f'Member area - Welcome {request.user.first_name}!')
    else:
        messages.error(request, 'Please login to access member area')
        return redirect('home')