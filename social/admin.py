from django.contrib import admin
from .models import SocialPost, SocialComment, Image

admin.site.register(SocialPost)
admin.site.register(SocialComment)
admin.site.register(Image)
# Register your models here.
