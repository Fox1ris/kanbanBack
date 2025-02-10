from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.shortcuts import render, get_object_or_404

from . import models

def user_profile(request):
    user_id = request.user.id
    user_infor = get_object_or_404(User, id=user_id)
    print(user_infor.get_full_name())
    return render(request, 'profile/profile.html', {'user_infor': user_infor})

