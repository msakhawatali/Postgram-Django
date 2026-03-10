from django.urls import path
from main import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("contact", views.contactpage, name="contact"),
    path("about", views.aboutpage, name="about"),
    path("services", views.servicespage, name="services"),
    path("post-is/<int:x>", views.onepost, name = "onepost"),
    path('like/<int:id>/', views.like_post, name="like_post"),
]