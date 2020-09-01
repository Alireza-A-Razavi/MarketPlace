import json

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.response import Response


from .serializers import CategorySerializer, CategoryDetailSerializer, VariationDetailSerializer, MainCategorySerializer
from .models import Category, Variation, CategoryVariation, MainCategory

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


class CategoryListView(ListAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = CategoryDetailSerializer
    lookup_field = 'title'
    queryset = Category.objects.all()
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

def category_list_view(request):
    categories = Category.objects.all()
    serialized_data = CategorySerializer(categories, many=True).data
    main_categories = MainCategory.objects.all()
    serialized_main_categories_data = MainCategorySerializer(main_categories, many=True).data
    categories_json_string = json.dumps(serialized_data)
    main_categories_json_string = json.dumps(serialized_main_categories_data)
    context = {
        'categories' : categories_json_string,
        'main_categories' : main_categories_json_string,
    }
    return render(request, 'views/template/header.html', context)



