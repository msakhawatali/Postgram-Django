from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
    userr = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="userprofile", null=True, blank=True)

class userPost (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="userpost", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_private = models.BooleanField(default=False)
    post = models.TextField(null=True, blank=True)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    tags = models.TextField(null=True, blank=True)
    image = models.BooleanField(default= True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(userPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['user', 'post']