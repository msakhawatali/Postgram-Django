from user_profile.models import userProfile

def user_profile(request):
    user_is = None
    if request.user.is_authenticated:
        try:
            user_is = userProfile.objects.get(userr=request.user)
        except userProfile.DoesNotExist:
            user_is = None
    return {'user_is': user_is}