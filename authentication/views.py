from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from user_profile.models import userProfile

# Create your views here.

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def signuppage(request):
    return render(request, 'signup.html')

def signupurl(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        f_name = data.get('f_name')
        l_name = data.get('l_name')
        password = data.get('password')

        user = User.objects.create_user(username = username, email = email, first_name = f_name, last_name = l_name, password = password)

        userProfile.objects.create( userr = user )

        messages.success(request, "Signup Done, Please Login to Continue...")

        return redirect('/auth/login')
    
def loginurl(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        check = authenticate(username = username, password = password)

        if check:
            login(request, check)            
        else:
            messages.warning(request, "Please enter vaild credentials...")
            return redirect("/auth/login")

        return redirect ("/")

def logouturl(request):
    logout(request)
    return redirect ("/auth/login")