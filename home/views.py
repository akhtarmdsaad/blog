from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse,render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserLoginForm,UserRegistration


# Create your views here.
def homepage(request):
    return render(request,"home/home.html")

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    elif request.method == "POST":
        form=UserLoginForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("home"))
        
    else:
        form = UserLoginForm()
    context = {
        "form":form
        }
    return render(request,"home/login.html",context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def user_registration(request):
    if request.method=="POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password"]
            new_user = User(first_name=first_name,last_name=last_name,email=email,username=username)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            messages.error(request,"Registration Unsuccessful. Please Enter data correctly")
    else:
        form = UserRegistration()
    context = {"form":form}
    return render(request,"home/register.html",context)

def me(request):
    user = request.user
    context = {"user":user}
    return render(request,"home/me.html",context)