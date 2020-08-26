from rest_framework import serializers

from .models import OrderItem, Order

from products.serializers import ProductDetailSerializer
from users.serializers import UserSerializer, ProducerProfileDetailSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'ordered',
            'quantity',
            'product',
            'user',
        )

    def get_product(self, obj):
        return ProductDetailSerializer(obj.item).data

    def get_user(self, obj):
        user = UserSerializer(obj.user).data




class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'ref_code',
            'start-dat',
            'ordered_date',
            'ordered',
        )

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.items.all(), many=True).data


