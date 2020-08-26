from rest_framework import serializers

from .models import Product, ProductVariation, Variation , ProductComment, Rating

from users.serializers import UserSerializer
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    sample = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'discount_price',
            'product_image',
            'slug',
            'stock',
            'description',
            'minimum_order',
            'payment_type',
            'packing',
            'shipping',
            'origin',
            'made_in',
            'delivery',
            'sample',
            'remarks',
        )

    def get_sample(self, obj):
        return obj.get_samples_display()

class ProductDetailSerializer(serializers.ModelSerializer):
    sample = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'discount_price',
            'product_image',
            'slug',
            'stock',
            'description',
            'minimum_order',
            'payment_type',
            'packing',
            'shipping',
            'origin',
            'made_in',
            'delivery',
            'sample',
            'remarks',
            'category',
            'average_rating',
            'get_comments',
            'user',
        )

    def get_sample(self, obj):
        return obj.get_samples_display()

    def get_category(self, obj):
        return CategorySerializer(obj.category.all(), many=True).data

    def get_user(self, obj):
        return UserSerializer(obj.producer).data



class ProductCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductComment
        fields = (
            'id',
            'is_confirmed',
            'content',
            'user',
            'product',
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'starts', 'user', 'product')



class ProductDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'discount_price',
            'product_image',
            'slug',
            'stock',
            'description',
            'minimum_order',
            'payment_type',
            'packing',
            'shipping',
            'origin',
            'made_in',
            'delivery',
            'samples',
            'remarks',
            'category',
            'average_rating',
            'producer',
            'comments',
        )

    def get_comments(self, obj):
        return ProductCommentSerializer(obj.productcomment_set.all(), many=True).data