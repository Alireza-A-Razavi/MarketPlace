import json

from django.views.generic import View
from django.shortcuts import render


#COMPONENTS
from products.models import Product
from proucts.serializers import ProductDetailSerializer, ProductSerializer

from categories.models import Category, MainCategory
from categories.serializers import CategorySerializer, MainCategorySerializer

from blog.models import  Post
from blog.serializers import PostSerializer

class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/front-end-render.html', {})


class IndexView(View):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        categories = Category.objects.all()
        main_categories = MainCategory.objects.all()
        posts = Post.objects.all().[:3]
        products_ser = ProductDetailSerializer(products, many=True).data
        categories_ser = CategorySerializer(categories, many=True).data
        main_categories_ser = MainCategorySerializer(main_categories, many=True).data
        post_ser = PostSerializer(posts, many=True).data
        products_ser_json = json.dumps(products_ser)
        categories_ser_json = json.dumps(categories_ser)
        main_categories_ser_json =json.dumps(main_categories_ser)
        post_ser_json = json.dumps(post_ser)

        context = {
            'products' : products_ser_json,
            'categories' : categories_ser_json,
            'main_categories' : main_categories_ser_json,
            'posts' : post_ser_json,
        }
        return render(self.request, "views/index.html", context)

