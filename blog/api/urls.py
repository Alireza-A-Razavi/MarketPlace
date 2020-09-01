from django.urls import path

from blog.views import PostListView, PostCreationView, CommentCreateView, CommentListView, PostDetailView, CreateCommentsView

app_name = 'blog-api'

urlpatterns = [
    path('postlist/', PostListView.as_view(), name='posts-list'),
    path('create/', PostCreationView.as_view(), name="post-creation"),
    path('comments/<post_name>/', CommentListView.as_view(), name="post-comment"),
    path('posts/<slug>/', PostDetailView.as_view(), name='post-detail'),
    path('comment/create/', CreateCommentsView.as_view(), name='comment-create'),
]