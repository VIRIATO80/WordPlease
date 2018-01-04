from rest_framework.permissions import BasePermission


class BlogPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False


class MyBlogPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False

