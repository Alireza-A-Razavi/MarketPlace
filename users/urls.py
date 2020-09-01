from django.urls import path

app_name = 'users'

from . import views

urlpatterns = [
    path('profile/', views.complete_prod_profile, name="profile"),
]