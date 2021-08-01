from django.urls import path

from .views import UserProfileView

app_name="accounts"

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),
]
