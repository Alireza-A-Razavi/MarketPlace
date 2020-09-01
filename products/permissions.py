from rest_framework import permissions
from .models import ProducerProfile


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        producer = ProducerProfile.objects.get(user=request.user)
        return obj.producer == producer


class IsProducer(permissions.BasePermission):
    message = "You ain't no producer dawg!"

    def has_permission(self, request, view):
        role = request.user.role
        if role == 'خریدار':
            return False
        else:
            return True

