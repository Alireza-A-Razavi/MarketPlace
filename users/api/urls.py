from django.urls import path, include
from rest_framework import routers
from users import views
from django.conf.urls import url

app_name = 'users-api'

urlpatterns = [
   path('user-id/', views.UserIDView.as_view(), name='user-id'),
   path('producer_profile/<pk>/', views.ProducerProfileRUDView.as_view(), name='producer_profile'),
   path('profile/<username>/', views.ProfileRUDView.as_view(), name='profile'),
   path('profile-creation/', views.ProfileCreateView.as_view(), name='profile_creation'),
   path('producer-profile-creation/', views.ProducerProfileCreateView.as_view(), name="producer_profile_creation"),
   path('singup/', views.sing_up),
]