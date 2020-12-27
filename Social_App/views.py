from django.shortcuts import render,redirect
# from Social_App.models import User_Resistrations
# from Social_App.forms import UserResistrationForm,UserLoginForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_view(request):
    return render(request,'login.html')

def login_authentication(request):
    if request.method == 'POST':
        U_name = request.POST['U_name']
        U_password = request.POST['U_password']
        user = authenticate(username=U_name,password=U_password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Hey {U_name},You Are Successfully Log In !!')
            return redirect('/welcome_view')
        else:
            messages.warning(request,'Some Credienties Not Match , Plz Try Again !!')
            return redirect('/')
   

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['e_username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password != password1:
            messages.warning(request,'Your Password & Re-Password Not Match , Plz Try Again !!')
            return redirect('/signup_view')
        else:
            myuser = User.objects.create_user(username,email,password1)
            myuser.save()
            return redirect('/')
    else:
        return render(request,'signup.html')


def welcome_view(request):
    return render(request,'welcome.html')

def add_post(request):
    return render(request,'add_post.html')



