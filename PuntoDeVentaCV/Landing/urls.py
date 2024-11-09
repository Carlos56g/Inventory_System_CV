from django.urls import path
from . import views


app_name="landing"
urlpatterns = [
    path("", views.landing, name="landing"),
    path("signIn", views.register, name="signIn"),
    path("logIn", views.LoginUserView.as_view(), name="logIn"),
    path("logOut", views.logOutUser, name="logOut"),
]

