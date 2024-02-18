from rest_framework.permissions import BasePermission
class MyCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=='POST':
            return True
        else:
            return False