from django.urls import path

app_name = 'products'

from . import views

urlpatterns = [
    path('', views.products_list_view, name="products"),
    path('users/', views.user_panel_view, name='userpanel'),
    path("<slug>/", views.product_detail_view, name="products-datail"),
]