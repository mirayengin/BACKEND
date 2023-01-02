from rest_framework.permissions import BasePermission,SAFE_METHODS





class IsAdminOrReadOnly(BasePermission):
  # SAFE_METHODS = ("GET","HEAD") #? burdada tanımlayabiliriz


    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )