from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.models import User


@csrf_exempt
def user(request):
    if request.method == 'GET':
        print('GET 查询')
        print(request.GET.get('username'))
        return HttpResponse('GET OK')
    if request.method == 'POST':
        print('POST 查询')
        return HttpResponse('POST OK')
    if request.method == 'PUT':
        print('PUT 查询')
        return HttpResponse('PUT OK')
    if request.method == 'DELETE':
        print('DELETE 查询')
        return HttpResponse('DELETE OK')


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self,request, *args,**kwargs):
        user_id = kwargs.get('id')

        if user_id:
            user_info = User.objects.filter(pk=user_id).values('username', 'gender')
            if user_info:
                return JsonResponse({
                    'status':200,
                    'message':'查询单个用户成功',
                    'results':list(user_info)
                })
            return JsonResponse({
                'status':400,
                'message':'查询失败',
            })
        else:
            user_infos = list(User.objects.all().values())
            if user_infos:
                return JsonResponse({
                    'status':200,
                    'message':'查询多个用户成功',
                    'results':user_infos
                })
            return JsonResponse({
                'status':400,
                'message':'查询失败',
            })


    def post(self,request, *args,**kwargs):
        print('post 插入数据')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.create(username=username,password=password)
            return JsonResponse({
                'status': 200,
                'message':'新增单个用户成功',
                'results': {'username':user_obj.username,'gender':user_obj.gender}

            })
        except:
            return JsonResponse({
                'status': 400,
                'message': '新增失败',
            })

    def put(self,request, *args,**kwargs):
        print('put 更新')
        return HttpResponse('put OK')

    def delete(self,request, *args,**kwargs):
        user_id = kwargs.get('id')
        print(user_id,111)
        if user_id:
            try:
                u = User.objects.filter(pk=user_id)
                if u:
                    u.delete()
                    return JsonResponse({
                        'status':200,
                        'message':'删除了id为%s的数据' %(user_id)
                    })
                return JsonResponse({
                        'status':400,
                        'message':'id不存在'
                    })
            except:
                return JsonResponse({
                    'status': 400,
                    'message': '删除失败',
                })
        return JsonResponse({
            'status':400,
            'message':'没有指定删除的id',
        })

    def patch(self,request,*args,**kwargs):
        print('patch 局部更新')
        return HttpResponse('patch ok')


# from rest_framework import views
# from rest_framework import serializers
# from rest_framework import status
# from rest_framework import permissions
# from rest_framework import throttling
# from rest_framework import authentication  #认证
# from rest_framework import filters   # 过滤器
# from rest_framework import pagination,parsers


# drf 开发视图

class StudentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print('drf give you')
        return Response('drf get ok')

    def post(self, request, *args, **kwargs):
        print('post')
        return Response('drf post ok')

    def put(self, request, *args, **kwargs):
        print('put')
        return Response('drf put ok')

    def delete(self, request, *args, **kwargs):
        print('delete')
        return Response('delete')

    def patch(self, request, *args, **kwargs):
        print('patch')
        return Response('patch')

