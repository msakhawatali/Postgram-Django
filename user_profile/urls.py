from django.urls import path
from user_profile import views

urlpatterns = [
    path('your-profile', views.userprofile, name="userprofile"),
    path('update-profile', views.updateprofile, name="updateprofile"),

    # Change password
    path('change-password', views.change_password, name="changepassword"),

    # add post
    path('add-post', views.add_post, name="addpost"),
    path('add-image', views.add_image, name="addimage"),
    path('upload-image-to-db', views.upload_image, name="uploadinmg"),
    path('upload-post-to-db', views.upload_post, name="uploadpost"),

    path("delete-post/<int:x>", views.delete_post, name = "deletepost"),
    path("chnage-to/<int:x>", views.change_to_post, name = "change_topost"),

]