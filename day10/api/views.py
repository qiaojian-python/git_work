from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import mixins

# 让标准http请求映射到自己定义的函数
from rest_framework import viewsets


from api.models import Book, TUser
from api.serializers import BookModelSerializer, BookModelDeSerializer, BookModelSerializerV2, UserModelSerializer


class BookAPIView(APIView):

    def get(self,request, *args, **kwargs):

        book_id = kwargs.get('id')
        if book_id:
            book_obj = Book.objects.filter(pk=book_id,is_delete=False)
            if book_obj:
                book_data = BookModelSerializer(book_obj[0]).data
                return Response({
                    'status': 200,
                    'message': '查询单个图书成功',
                    'results': book_data
                }, status=200)
            else:
                return Response({
                    'status': 400,
                    'message': '查询失败',
                }, status=400)
        else:
            book_obj_all = Book.objects.filter(is_delete=False)
            book_data = BookModelSerializer(book_obj_all,many=True).data
            return Response({
                'status':200,
                'message':'查询所有成功',
                'results':book_data
            },status=200)

    # 添加数据
    def post(self, request, *args, **kwargs):

        book_data = request.data
        if isinstance(book_data, dict) and book_data != {}:
            many = False
        elif isinstance(book_data, list) and book_data != []:
            many = True
        else:
            return Response({
                'status':400,
                'message':'参数格式有误',
            },status=400)

        book_ser = BookModelDeSerializer(data=book_data, many=many)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()
        return Response({
            'status': 200,
            'message': '新增成功',
            'results': BookModelSerializer(book_obj, many=many).data
        },status=200)


#     删除数据 将字段is_delete改为True
    def delete(self, request, *args, **kwargs):
        # print(111)
#         删除单个
        book_id = kwargs.get('id')
        t = request.data.get('ids')
        if book_id:
            ids = [book_id]
        elif isinstance(t,list):
            ids = t
        else:
            return Response({
                'status': 400,
                'message': '参数格式有误',
            }, status=400)

        # 对ids里的id更新字段
        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        print(response,123)
        if response:
            return Response({
                "status": 200,
                "message": '删除成功'
            },status=200)

        return Response({
                "status": 400,
                "message": '删除失败'
            },status=400)

#     更新 全部字段
    def put(self, request, *args, **kwargs):
#         获得更新的图书的id
        book_id = kwargs.get('id')
#         获取要修改的数据
        book_data = request.data
        print(book_data)

        if book_id:
            book_obj = Book.objects.filter(pk=book_id,is_delete=False)[0]
            if not book_obj:
                return Response({
                    "status": 400,
                    "message": '图书不存在'
                },status=400)
        #     使用反序列器进行更新
            serializer = BookModelDeSerializer(data=book_data, instance=book_obj)
            serializer.is_valid(raise_exception=True)
            obj = serializer.save()
            return Response({
                'status':200,
                'message':'更新成功',
                "results":BookModelSerializer(obj).data
            },status=200)
        else:
            return Response({
                "status": 400,
                "message": '无id'
            }, status=400)


#       部分更新一个对象
    def patch(self, request, *args, **kwargs):
        #         获得更新的图书的id
        book_id = kwargs.get('id')
        #         获取要修改的数据
        book_data = request.data
        print(book_data)

        if book_id:
            book_obj = Book.objects.filter(pk=book_id, is_delete=False)[0]
            if not book_obj:
                return Response({
                    "status": 400,
                    "message": '图书不存在'
                }, status=400)
            #     使用反序列器进行更新
            serializer = BookModelDeSerializer(data=book_data, instance=book_obj, partial=True)
            serializer.is_valid(raise_exception=True)
            obj = serializer.save()
            return Response({
                'status': 200,
                'message': '更新成功',
                "results": BookModelSerializer(obj).data
            }, status=200)
        else:
            return Response({
                "status": 400,
                "message": '无id'
            }, status=400)
        pass

# 序列器与反序列器整合的版本
class BookAPIViewV2(APIView):

    def get(self,request, *args, **kwargs):

        book_id = kwargs.get('id')
        if book_id:
            book_obj = Book.objects.filter(pk=book_id,is_delete=False)
            if book_obj:
                book_data = BookModelSerializerV2(book_obj[0]).data
                return Response({
                    'status': 200,
                    'message': '查询单个图书成功',
                    'results': book_data
                }, status=200)
            else:
                return Response({
                    'status': 400,
                    'message': '查询失败',
                }, status=400)
        else:
            book_obj_all = Book.objects.filter(is_delete=False)
            book_data = BookModelSerializerV2(book_obj_all,many=True).data
            return Response({
                'status':200,
                'message':'查询所有成功',
                'results':book_data
            },status=200)

    # 添加数据
    def post(self, request, *args, **kwargs):

        book_data = request.data
        if isinstance(book_data, dict) and book_data != {}:
            many = False
        elif isinstance(book_data, list) and book_data != []:
            many = True
        else:
            return Response({
                'status':400,
                'message':'参数格式有误',
            },status=400)

        book_ser = BookModelSerializerV2(data=book_data, many=many)
        book_ser.is_valid(raise_exception=True)
        book_obj = book_ser.save()
        return Response({
            'status': 200,
            'message': '新增成功',
            'results': BookModelSerializerV2(book_obj, many=many).data
        },status=200)


#     删除数据 将字段is_delete改为True
    def delete(self, request, *args, **kwargs):
        # print(111)
#         删除单个
        book_id = kwargs.get('id')
        t = request.data.get('ids')
        if book_id:
            ids = [book_id]
        elif isinstance(t,list):
            ids = t
        else:
            return Response({
                'status': 400,
                'message': '参数格式有误',
            }, status=400)

        # 对ids里的id更新字段
        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        print(response,123)
        if response:
            return Response({
                "status": 200,
                "message": '删除成功'
            },status=200)

        return Response({
                "status": 400,
                "message": '删除失败'
            },status=400)

#     更新 全部字段
    def put(self, request, *args, **kwargs):
#         获得更新的图书的id
        book_id = kwargs.get('id')
#         获取要修改的数据
        book_data = request.data
        print(book_data)

        if book_id:
            book_obj = Book.objects.filter(pk=book_id,is_delete=False)[0]
            if not book_obj:
                return Response({
                    "status": 400,
                    "message": '图书不存在'
                },status=400)
        #     使用反序列器进行更新
            serializer = BookModelSerializerV2(data=book_data, instance=book_obj)
            serializer.is_valid(raise_exception=True)
            obj = serializer.save()
            return Response({
                'status':200,
                'message':'更新成功',
                "results":BookModelSerializerV2(obj).data
            },status=200)
        else:
            return Response({
                "status": 400,
                "message": '无id'
            }, status=400)


# 更新一个部分对象
#       部分更新一个对象
#     def patch(self, request, *args, **kwargs):
#         #         获得更新的图书的id
#         book_id = kwargs.get('id')
#         #         获取要修改的数据
#         book_data = request.data
#         print(book_data)
#
#         if book_id:
#             book_obj = Book.objects.filter(pk=book_id, is_delete=False)[0]
#             if not book_obj:
#                 return Response({
#                     "status": 400,
#                     "message": '图书不存在'
#                 }, status=400)
#             #     使用反序列器进行更新
#             serializer = BookModelSerializerV2(data=book_data, instance=book_obj, partial=True)
#             serializer.is_valid(raise_exception=True)
#             obj = serializer.save()
#             return Response({
#                 'status': 200,
#                 'message': '更新成功',
#                 "results": BookModelSerializerV2(obj).data
#             }, status=200)
#         else:
#             return Response({
#                 "status": 400,
#                 "message": '无id'
#             }, status=400)
#         pass

# 更新部分群体对象
    def patch(self, request, *args, **kwargs):
#         request_data = request.data
#         book_id = kwargs.get('id')
#
#         #  修改单个
#         if book_id and isinstance(request_data, dict):
#             book_ids = [book_id]
#             request_data = [request_data]
#         #  修改多个
#         elif not book_id and isinstance(request_data, list):
#             book_ids = []
#             for dic in request_data:
#                 pk = dic.pop("id",None)
#                 if pk:
#                     book_ids.append(pk)
#                 else:
#                     return Response({
#                         'status':400,
#                         'message':'pk不存在'
#                     },status=400)
#         else:
#             return Response({
#                 'status': 400,
#                 'message': '参数有误'
#             }, status=400)
#
# #         所有要修改的图书对象
#         book_list = []
#         new_data = []
#         for index,pk in enumerate(book_ids):
#             try:
#                 book_obj = Book.objects.get(pk=pk)
#                 book_list.append(book_obj)
#                 new_data.append(request_data[index])
#             except Exception:
#                 pass
#
# #         将单个修改转换成群体修改
#         book_ser = BookModelSerializerV2(data=new_data,instance=book_list, partial=True, many=True)
#         book_ser.is_valid(raise_exception=True)
#         book_ser.save()
#         return Response({
#             'status': 200,
#             'message': 'success'
#         }, status=200)
        request_data = request.data
        book_id = kwargs.get('id')
        # 如果id存在且传递的request.data格式是字典 单个修改 转换成群体修改一个
        if book_id and isinstance(request_data, dict) and request_data != {}:
            book_ids = [book_id]
            request_data = [request_data]
        elif not book_id and isinstance(request_data, list) and request_data != []:
            book_ids = []
            for dic in request_data:
                pk = dic.pop("id",None)
                if pk:
                    book_ids.append(pk)
                else:
                    return Response({
                        "status": status.HTTP_400_BAD_REQUEST,
                        'message':"pk不存在"
                    })
        else:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                'message': "参数格式有误",
            })
        # 进行筛选
        book_list = []
        new_data = []
        for index, pk in enumerate(book_ids):
            try:
                book_obj = Book.objects.get(pk=pk)
                book_list.append(book_obj)
                new_data.append(request_data[index])
            except Book.DoesNotExist:
                pass
        book_ser = BookModelSerializerV2(data=new_data, instance=book_list, partial=True, many=True)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()
        return Response({
            'status':200,
            'message':'success'
        })



# class BookGenericAPIView(GenericAPIView):
#     queryset = Book.objects.filter(is_delete=False)
#     serializer_class = BookModelSerializerV2
#     lookup_field = "id"
#
#     def get(self, request, *args, **kwargs):
#         if "id" in kwargs:
#             print(kwargs)
#             book_obj = self.get_object()
#             serializer = self.get_serializer(book_obj, many=False)
#             return Response({
#                 "status":200,
#                 "message":"查询单个图书成功",
#                 "results":serializer.data
#             })
#         else:
#     #         查询所有
#     #         获取book模型中所有的数据
#             book_list = self.get_queryset()
#     #         获取序列化器
#             serializer = self.get_serializer(book_list, many=True)
#             return Response({
#                 "status":200,
#                 "message":"查询所有图书成功",
#                 "results":serializer.data
#             })

class BookGenericAPIView(GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin
                         ):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializerV2
    lookup_field = "id"

#     工具查询所有
    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



#     def get(self, request, *args, **kwargs):
#         # 查询单个
#         if "id" in kwargs:
#             book_obj = self.get_object()
#             serializer = self.get_serializer(book_obj, many=False).data
#             return Response({
#                 "status": 200,
#                 "message": "查询单个图书成功",
#                 "results": serializer
#             })
#         # 查询所有
#         # 获取book模型中的数据
#         book_list = self.get_queryset()
# #         获取序列化器
#         serializer = self.get_serializer(book_list, many=True).data
#         return Response({
#             "status":200,
#             "message": "查询所有图书成功",
#             "results":  serializer
#         })


# 工具视图，继承方便使用
class BookGenericAPIView2(generics.ListAPIView,
                          generics.RetrieveUpdateDestroyAPIView,
                          generics.CreateAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializerV2
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)



# 发起post请求， 不想执行标准http操作 完成登陆

class BookViewSetView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializerV2
    lookup_field = "id"

    def user_login(self, request, *args, **kwargs):
#         在此完成登录的逻辑
        request_data = request.data
        print(request_data)
        return Response({
            'status':status.HTTP_200_OK,
            'message':'登录成功'
        })

#     完成查询
    def get_user_count(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)



# 		注册接口  登陆接口


class UserViewSetView(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin):
    queryset = TUser.objects.filter(is_delete=False)
    serializer_class = UserModelSerializer
    lookup_field = "id"

    # post登录就是查询,根据表单或json传入用户名密码
    def user_login(self, request, *args, **kwargs):
#         在此完成登录的逻辑
        user_data = request.data
        instance = TUser.objects.filter(**user_data)
        if instance:
            serializer = self.get_serializer(instance[0])
            # dic = {"username":serializer.data['username']}
            return Response({
                'status':status.HTTP_200_OK,
                'message':'登录成功',
                'results':serializer.data
            },status=200)
        else:
            return Response({
                'status':400,
                'message':'用户名或密码错误'
            })

#     post注册就是create
    def user_regist(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#     完成查询
    def get_user_count(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)



