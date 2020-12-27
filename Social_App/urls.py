from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.login_view,name="login_view"),
    path('login_authentication/',views.login_authentication,name="login_authentication"),
    path('signup_view/',views.signup_view,name="signup_view"),
    path('welcome_view/',views.welcome_view,name="welcome_view"),
    path('add_post/',views.add_post,name="add_post"),
]
