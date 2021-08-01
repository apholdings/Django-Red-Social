from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from accounts.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfileView(View):
    def get(self, request, username,*args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)

        context={
            'user':user,
            'profile':profile
        }
        return render(request, 'users/detail.html', context)