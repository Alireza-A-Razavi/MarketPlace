from django.urls import path

app_name = 'users'

from . import views

urlpatterns = [
    path('profile/', views.complete_prod_profile, name="profile"),
    path('customer/profile/', views.customer_profile_completion, name="customer-profile"),
]