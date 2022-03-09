# 自定义权限

from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员可进行修改
    其他用户仅可查看
    """
    def has_permission(self, request, view):
        # 对所有人允许GET，HEAD，等请求
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser