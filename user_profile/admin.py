from django.contrib import admin
from user_profile.models import userProfile, userPost

# Register your models here.

admin.site.register(userProfile)
admin.site.register(userPost)