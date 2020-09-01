from rest_framework import permissions
from .models import ProducerProfile

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        producer = ProducerProfile.objects.get(user=request.user)
        # Write permissions are only allowed to the owner of the snippet.
        return obj.producer == producer


class IsProducer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return False

        return obj.producer.user.role == "خریدار"

