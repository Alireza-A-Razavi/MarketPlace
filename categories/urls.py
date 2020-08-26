from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name="categories_list"),
    path('<title>/', views.CategoryDetailView.as_view(), name="category_details"),
]