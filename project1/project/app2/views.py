from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    # if request.method =='POST':
    #     username = request.POST['username']
    #     password = 

    return render(request,'login.html')

def logout(request):
    pass

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        passsword = request.POST['passsword']
        confirm_password = request.POST['confirm_password']
        if passsword==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Email exists')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,password=passsword, email=email, first_name=first_name, last_name=last_name)
                user.set_password(passsword)
                user.save()
                print("Success")
                return redirect('login')
        else:
            print("no post method")
    return render(request,'register.html')
