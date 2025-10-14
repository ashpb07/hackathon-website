from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.models import User


def singin(request):
     return HttpResponse('sigin')
     if request.method =='POST':
        
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
    
            messages.success(request,'sucess')
            return redirect('member')  

        else:
            messages.error(request,"invalid")
            return redirect('signin')
    

        return HttpResponse('signed in')
     










def logout(request):
    return HttpResponse('logout')

    logout(request)
    return redirect('home')
    return HttpResponse('logout')


def singup(request):
       return HttpResponse('sigout')
        
       if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        if User.objects.filter(username=username):
                messages.error(request,"username already exists")
                return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request,"email already exists")
            return redirect('signup')    

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        


        messages.success(request, "Signup successful!")



        # subject="welcome to The Poet's Archive"
        # message="hello,"+myuser.first_name
        # from_email=settings.EMAIL_HOST_USER
        # to_list=[myuser.email]
        # email = EmailMessage(
        #     subject=subject,
        #         body='Hello,'+myuser.first_name,
        # from_email=settings.EMAIL_HOST_USER,
        #     to=[myuser.email],
        # )
        

        
        # email.send()
        return HttpResponse('signup done')