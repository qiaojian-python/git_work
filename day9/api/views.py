from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Book
from api.serializers import BookModelSerializer, BookModelDeSerializer, BookModelSerializerV2

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
            serializer = BookModelSerializerV2(data=book_data, instance=book_obj, partial=True)
            serializer.is_valid(raise_exception=True)
            obj = serializer.save()
            return Response({
                'status': 200,
                'message': '更新成功',
                "results": BookModelSerializerV2(obj).data
            }, status=200)
        else:
            return Response({
                "status": 400,
                "message": '无id'
            }, status=400)
        pass








