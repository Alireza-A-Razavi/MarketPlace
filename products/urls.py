from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ProductViewSet

from . import views

app_name = 'products'

router = routers.DefaultRouter()
router.register('products',ProductViewSet)

urlpatterns = [
    path('', views.ProductListView.as_view(), name="product_list"),
    path('<company_name>/', views.ProducerProductPublicListView.as_view(), name='producer_products'),
    path('my_products/', views.ProducersProductListView.as_view(), name='my_products'),
    # path('my_products/<title>/', views.ProducerProductDetailView.as_view(),)
    path('', include(router.urls)),
    path('category/<category>/', views.ProductsByCategory.as_view(), name="product-category"),
    path('search/filter/', views.VueFilterView.as_view(), name='filter'),
]

# from django.urls import path
# from .views import ProductViewSet, api_root
# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
#
# porduct_list = ProductViewSet.as_view(
#     {'get': 'list',
#      'post': 'create'}
# )
#
# porduct_detail = ProductViewSet.as_view(
#     {
#         'get': "retrieve",
#         'put': "update",
#         'path': "partial_update",
#         'delete': "destroy"
#     }
# )
#
# product_rate_product = ProductViewSet.as_view(
#     {
#         'get': 'rate_product',
#         'post': "rate_product",
#
#     }, renderer_classes=[renderers.StaticHTMLRenderer]
# )
#
# product_comments = ProductViewSet.as_view(
#     {
#         'get': 'comment_on_product',
#         'post': 'comment_on_product',
#     },
# )
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', porduct_list, name='product-list'),
#     path('snippets/<str:name>/<int:pk>/', porduct_detail, name='product-detail'),
#     path('snippets/<str:name>/<int:pk>/rate_product/', product_rate_product, name='product-highlight'),
#     path('products/<str:name>/<int:pk>/comment/', product_comments, name='product-comments'),
# ])









