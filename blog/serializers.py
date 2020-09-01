from rest_framework import serializers

from .models import Post, Comment

from users.serializers import UserSerializer


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

#POSTS
class PostSerializer(serializers.ModelSerializer):
    categories = StringSerializer(many=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'short_description',
            'content',
            'timestamp',
            'thumbnail',
            'categories',
            'featured',
            'active_post',
            'slug',
            'author',
        )
        read_only_fields = ['pk', 'featured']

    def get_author(self, obj):
        return UserSerializer(obj.author).data

#COMMENTS

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    post = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'timestamp',
            'content',
            'user',
            'post',
        )
        read_only_fields = ['pk', 'user']

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_post(self, obj):
        return PostSerializer(obj.post).data



class PostDetailSerializer(serializers.ModelSerializer):
    categories = StringSerializer(many=True)
    author = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'short_description',
            'content',
            'timestamp',
            'thumbnail',
            'categories',
            'featured',
            'active_post',
            'slug',
            'author',
            # 'comments',
            'get_comment',
        )

    def get_author(self, obj):
        return UserSerializer(obj.author).data

    def get_comments(self, obj):
        return CommentSerializer(obj.comment_set.all(), many=True).data


class CommentsUndetailedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'user',
            'timestamp',
            'post'
        )