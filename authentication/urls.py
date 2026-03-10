from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.loginpage, name="login"),
    path('signup', views.signuppage, name="signup"),

    # auth urls
    path('signup-url', views.signupurl, name="signupurl"),
    path('login-url', views.loginurl, name="loginurl"),
    path('logout-url', views.logouturl, name="logouturl"),
]