from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.homepage,name="home"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name = "logout"),
    path("register/",views.user_registration,name="register"),
    path("me/",views.me,name="me"),
]