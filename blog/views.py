import json

from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import PostSerializer, CommentSerializer, PostDetailSerializer, CommentsUndetailedSerializer
from .models import Post, Comment

"""
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################      
"""
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

    def create(self, *args, **kwargs):
        post_comment = Comment.objects.create(user=self.request.user)
        post_comment.content = CommentSerializer(self.request.data["content"])
        post_name = self.kwargs['post_name']
        post = Post.objects.get(title=post_name)
        post_comment.post.id = post.id
        post_comment.save()


class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)


class CreateCommentsView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsUndetailedSerializer
"""
END OF:
################################################################
            ##          ############         ##
           ## #         ##        ##         ##
          ##   #        ##        ##         ##
         ##     #       ##        ##         ##
        ## # # # #      ############         ##
       ##         #     ##                   ##
      ##           #    ##                   ##
     ##             #   ##                   ##
##################################################################      
"""

# #posts list
# def post_list_view(request):
#     posts = Post.objects.all()
#     serialized = PostDetailSerializer(posts, many=True).data
#     posts_json_string = json.dumps(serialized)
#     return render(request, 'posts/post_list.html', { 'posts' : posts_json_string})
#


