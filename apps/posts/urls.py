from django.urls import path
from .views import PostListViews, PostDetailView
from . import views

app_name = 'apps.posts'

urlpatterns = [
    path('posts/', PostListViews.as_view(), name='posts'),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_individual"),
]
