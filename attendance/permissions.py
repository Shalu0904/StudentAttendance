from rest_framework.permissions import BasePermission
from .models import Teacher


class IsTeacher(BasePermission):
    def has_permission(self, request, view):

        return Teacher.objects.filter(user=request.user).exists()
