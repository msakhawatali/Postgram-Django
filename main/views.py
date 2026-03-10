from django.shortcuts import render, get_object_or_404, redirect
from user_profile.models import userPost, userProfile, Like
from main.models import contactUs
from django.contrib import messages

# Create your views here.

def homepage(request):
    user_is = None
    total_post = None

    if request.user.is_authenticated:
        user_is, created = userProfile.objects.get_or_create(userr=request.user)
        total_post = userPost.objects.filter(user=request.user).count()

    # Get all public posts
    query = request.GET.get('q', '')
    if query:
        feed = userPost.objects.filter(is_private=False, tags__icontains=query).order_by("-id") | \
            userPost.objects.filter(is_private=False, description__icontains=query).order_by("-id") | \
            userPost.objects.filter(is_private=False, user__username__icontains=query).order_by("-id")
        feed = feed.distinct()
    else:
        feed = userPost.objects.filter(is_private=False).order_by("-id")

    # Add user_liked boolean to each post
    for post in feed:
        if request.user.is_authenticated:
            post.user_liked = post.like_set.filter(user=request.user).exists()
        else:
            post.user_liked = False

    context = {
        "feed": feed,
        "user_is": user_is,
        "total_post": total_post,
        "query": query,
    }

    return render(request, "home.html", context)

def contactpage(request):
    if request.method == "POST":
        f_name = request.POST.get("full_name")
        emial = request.POST.get("email")
        msg = request.POST.get("msg")

        contactUs.objects.create(full_name = f_name, email = emial, message = msg)
        messages.success(request, 'Your message recived sucessfuly ! will contact you asap..!')

    return render(request, "contact.html")

def aboutpage(request):
    return render(request, "about.html")

def servicespage(request):
    return render(request, "services.html")


def onepost(request, x):
    post = userPost.objects.get(id = x)
    return render(request, "onepost.html", {"post" : post})

def like_post(request, id):
    post = get_object_or_404(userPost, id=id)
    like = Like.objects.filter(user=request.user, post=post)

    feed = userPost.objects.all()

    if like.exists():
        like.delete()      
    else:
        Like.objects.create(user=request.user, post=post) 

    return redirect("home")