from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.userlogin,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.userlogout,name="logout"),
    path('checkuser/',views.userChecker,name="checkuser"),
]
