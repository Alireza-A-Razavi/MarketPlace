from django.urls import path, include
from rest_framework.routers import DefaultRouter
from merchandise.views import OrderViewSet

app_name = 'merchandise-api'

router = DefaultRouter()
router.register('merchandise', OrderViewSet.as_view())

urlpatterns = [
    path('', include(router.urls))
]