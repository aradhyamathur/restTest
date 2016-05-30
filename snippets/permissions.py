from rest_framework import permissions

# # # creating custom permission for user operations
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.owner == request.user

