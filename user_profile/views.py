from django.shortcuts import render, redirect
from user_profile.models import userProfile, userPost
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Create your views here.
def userprofile(request):
    user_info = userProfile.objects.get(userr = request.user)
    user_data = userPost.objects.filter(user = request.user).order_by("-id")
    return render(request, 'profile.html', {'user_info': user_info, 'user_data' : user_data})

def updateprofile(request):
    userr = userProfile.objects.get(userr = request.user)
    current_user = User.objects.get(username = request.user)
    if request.method == "POST":
        img = request.FILES.get("profilepic")
        if img:
            userr.profile_pic = img
        else:
            userr.profile_pic = userr.profile_pic

        if request.POST.get("bio"):
            userr.bio = request.POST.get("bio") 

        if request.POST.get("address"):
            userr.address = request.POST.get("address") 

        if request.POST.get("p_num"):
            userr.phone_number = request.POST.get("p_num") 

        if request.POST.get("f_name"):
            current_user.first_name = request.POST.get("f_name")

        if request.POST.get("l_name"):
            current_user.last_name = request.POST.get("l_name")

        if request.POST.get("email"):
            current_user.email = request.POST.get("email")

        userr.save()
        current_user.save()
        
        return redirect("/profile/your-profile")

    return render(request, 'update_profile.html', {"user_info" : userr})


def change_password(request):
    current_user = User.objects.get(username = request.user)
    if request.method == "POST":
        old_pass = request.POST.get("o_pass")
        new_pass = request.POST.get("n_pass")
        confirm_pass = request.POST.get("c_pass")
        if new_pass != confirm_pass:
            messages.warning(request, "please match the passwords....!")
        else:
            if check_password(old_pass, current_user.password):
                current_user.set_password(new_pass)
                current_user.save()
                messages.success(request, "Password Updated Sucessfully..!")
            else:
                messages.warning(request, "Please enter old password valid")
    return redirect("/auth/login")


def add_post(request):
    return render(request, "upload_post.html")


def add_image(request):
    return render(request, "upload_image.html")

def upload_image(request):
    if request.method == "POST":
        img = request.FILES.get("img")
        tags = request.POST.get("tag")
        visibility = request.POST.get("visibility")
        desc = request.POST.get("desc")

        if visibility == "public":
            visibility = False 
        else:
            visibility = True

        userPost.objects.create(user = request.user ,img = img, description = desc, tags = tags, is_private = visibility)
    return redirect("/profile/add-post")

def upload_post(request):
        if request.method == "POST":
            tags = request.POST.get("tag")
            visibility = request.POST.get("visibility")
            desc = request.POST.get("desc")
            post = request.POST.get("post")

            if visibility == "public":
                visibility = False 
            else:
                visibility = True

            userPost.objects.create(user = request.user, description = desc, tags = tags, is_private = visibility, post = post, image = False)


        return redirect("/profile/add-post")


def delete_post(request, x):
    record = userPost.objects.get(id = x)
    record.delete()
    return redirect("/profile/your-profile")

def change_to_post(request, x):
    record = userPost.objects.get(id = x)
    record.is_private = not(record.is_private)
    record.save()
    return redirect("/profile/your-profile")