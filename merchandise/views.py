from rest_framework import viewsets, status, permissions, authentication

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (permissions.AllowAny, permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication,]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

class OrderItemSerializer(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = (permissions.AllowAny, permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication, ]

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.filter(user=user)