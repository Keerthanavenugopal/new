from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
        return redirect('login')
    return  render(request,"login.html")


def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                print("username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,last_name=lastname,first_name=firstname,email=email,password=password )
                user.save()
                return redirect('login')
                print("user created")

        else:
            print("password not matched")
            return redirect('register')
    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request,'form.html')

def loggedin(request):
    return render(request,'areyousure.html')

def submitted(request):
    return render(request, 'submitted.html')
