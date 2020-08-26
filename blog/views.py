from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

class PostCreationView(CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = (AllowAny, )


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    # permission_classes = (AllowAny,)

    def get_queryset(self):
        post_name = self.kwargs['post_name']
        return Comment.objects.filter(post__title=post_name)

class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        post_name = self.kwargs['post_name']
        return Comment.objects.filter(post__title=post_name)