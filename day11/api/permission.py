# 自定义权限类
# from rest_framework.permissions import BasePermission
#
# class MyPermission(BasePermission):
#     """
#     登录可写  游客只读
#     有权限返回True  无返回False
#     """
#     def has_permission(self, request, view):
#         pass

# 自定义权限
from rest_framework.permissions import BasePermission

from api.models import User

class MyPermission(BasePermission):
    """
    登录可写  游客只读
    有权限返回True 无权限返回False
    """

    def has_permission(self, request, view):
#         如果只读 所有人都可以访问
        if request.method in ("GET", 'HEAD', 'OPTIONS'):
            return True
        # print(111)
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        # print(user)
        if user:
            return True
        return False











