from django.urls import path

from .views import UserProfileView, EditProfile, AddFollower, RemoveFollower, ListFollowers

app_name="accounts"

urlpatterns = [
    path('<username>/', UserProfileView, name="profile"),
    path('profile/edit', EditProfile, name="edit-profile"),

    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
	path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),

    path('profile/<int:pk>/followers/',ListFollowers.as_view(), name='followers-list'),
]
