from django.urls import path

from .views import PostListView, PostCreationView, CommentCreateView, CommentListView

app_name = 'blog'

urlpatterns = [
    path('postlist/', PostListView.as_view(), name='posts-list'),
    path('create/', PostCreationView.as_view(), name="post-creation"),
    path('comments/<post_name>/', CommentListView.as_view(), name="post-comment"),
    path('comments/<post_name>/create/', CommentCreateView.as_view(), name="create-comment"),
]