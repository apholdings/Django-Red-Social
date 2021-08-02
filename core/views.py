from social.models import Image, SocialPost, SocialComment
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from social.forms import SocialPostForm, ShareForm


class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logged_in_user=request.user

        posts = SocialPost.objects.filter(author__profile__followers__in=[logged_in_user.id]).order_by('-created_on')

        form = SocialPostForm()
        share_form=ShareForm()

        
        context={
            'posts':posts,
            'form':form,
            'share_form':share_form
        }
        return render(request, 'pages/index.html', context)

    def post(self, request, *args, **kwargs):
        logged_in_user=request.user

        posts = SocialPost.objects.filter(
                author__profile__followers__in=[logged_in_user.id]
            ).order_by('-created_on')

        form = SocialPostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')

        share_form=ShareForm()

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = logged_in_user
            new_post.save()

            for f in files:
                img = Image(image=f)
                img.save()
                new_post.image.add(img)

            new_post.save()

        
        context={
            'posts':posts,
            'form':form,
            'share_form':share_form
        }
        return render(request, 'pages/index.html', context)


