from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


# class UserDetailAPIView(APIView):
#     """
#     只有登录以后才能访问
#     """
#     permission_classes = (IsAuthenticated)
#     # 认证校验token
#     authentication_classes = (JSONWebTokenAuthentication)
#     def get(self, request, *args, **kwargs):
#         return Response('ok')
from api.authentication import JWTAuthencation
from api.filter import ComputerFilterSet
from api.models import Computer
from api.pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from api.serializer import UserModelSerializer, ComputerModelSerializer


class UserDetailAPIView(APIView):
    """
    只能登陆后访问,有token
    """
    permission_classes = [IsAuthenticated]

    # 认证token
    authentication_classes = [JWTAuthencation]

    def get(self, request, *args, **kwargs):
        return Response("ok")


# 自定义签发视图
class LoginAPIView(APIView):
    """
    实现多方式登录 手机号 邮箱 用户名
     1 禁用权限与认证组件
     2 获取前端传递的参数
     3 校验前端传递的参数来得到对应的用户
     4 签发token 并返回

    """
    permission_classes = ()
    authentication_classes = ()


    def post(self, request, *args, **kwargs):
#         前端账号来传递用户标识  account 密码使用password
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = {
            'token': serializer.token,
            'user': UserModelSerializer(serializer.obj).data
        }
        return Response(data)


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer
#     通过filter_backends来配置要使用的 过滤器类
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

#     指定要搜索的字段/条件
    search_fields = ['name','price']
    # 指定排序的条件
    ordering = ['price']


    # 分页器的使用  需要定义分页器
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination


    # 查询价格大于3000 小于8000 的电脑
    filter_class = ComputerFilterSet

