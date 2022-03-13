from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):


    def has_permission(self, request, view):
        """未登录不能评论"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """验证评论的作者是否为登录用户，obj为当前评论"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
