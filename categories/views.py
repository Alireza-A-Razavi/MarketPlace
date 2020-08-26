from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.response import Response


from .serializers import CategorySerializer, CategoryDetailSerializer, VariationDetailSerializer
from .models import Category, Variation, CategoryVariation

class CategoryListView(ListAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = CategoryDetailSerializer
    lookup_field = 'title'
    queryset = Category.objects.all()



