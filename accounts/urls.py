from django.urls import path
from . views import *

app_name = "accounts"

urlpatterns = [
    path("login/",acc_login,name="login"),
    path("logout/",acc_logout,name="logout"),
    path("signup/",acc_signup,name="signup"),
]
