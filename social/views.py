from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from .models import SocialPost, SocialComment
from django.views.generic.edit import UpdateView, DeleteView



class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)


        context= {
            'post':post,
        }
        return render(request, 'pages/social/detail.html', context)

    def post(self, request, pk,*args, **kwargs):
        post = SocialPost.objects.get(pk=pk)

        context= {
            'post':post,
        }
        return render(request, 'pages/social/detail.html', context)



class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=SocialPost
    fields=['body']
    template_name='pages/social/edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk':pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=SocialPost
    template_name='pages/social/delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
