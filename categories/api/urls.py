from django.urls import path

from categories import views

app_name = 'categories-api'

urlpatterns = [
    path('', views.CategoryListView.as_view(), name="categories_list"),
    path('<title>/', views.CategoryDetailView.as_view(), name="category_details"),
]