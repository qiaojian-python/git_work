from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from api.models import Employee, Teacher
from api.serializers import EmployeeSerializer, EmployeeDeSerializer, TeacherSerializer, TeacherDeSerializer


class StudentAPIView(APIView):

    # 只返回json数据
    # renderer_classes = (JSONRenderer,)

    # 为某个视图单独指定接受的解析器
    # parser_classes = [JSONParser,MultiPartParser]

    def get(self, request ,*args, **kwargs):
        # 根据id 查询model对象
        emp_id = kwargs.get('id')
        if emp_id:
            # 查询单个
            emp_obj = Employee.objects.get(pk=emp_id)
        #     使用序列化器完成对象的序列化
            emp_seria = EmployeeSerializer(emp_obj)
            return Response({
                'status':200,
                'message':'查询单个员工成功',
                'results':emp_seria.data
            },status=200)
        else:
            emp_obj_all = Employee.objects.all()

        #     序列化多个对象时，需要指定属性many=True
        emp_data = EmployeeSerializer(emp_obj_all, many=True).data
        # print(emp_data)

        return Response({
            'status':200,
            'message':'查询所有员工成功',
            'results':emp_data
        })

    def post(self, request ,*args, **kwargs):

        # 获取前端传递的参数
        request_data = request.data

        # 前端传递的数据进行入库时 需要判断数据的格式是否合法
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                'status':400,
                'message':'参数有误'
            },status=400)

        serializer = EmployeeDeSerializer(data=request_data)
        if(serializer.is_valid()):
            emp_ser = serializer.save()

            return Response({
                'status':200,
                'message':'success',
                'results':EmployeeSerializer(emp_ser).data
            },status=200)
        else:
            return Response({
                'status':400,
                'message':'员工添加失败',
                'results':serializer.errors
            })


class TeacherAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # 根据id 查询model对象
        tea_id = kwargs.get('id')
        if tea_id:
            # 查询单个
            tea_obj = Teacher.objects.filter(pk=tea_id).first()
            if tea_obj:
                #     使用序列化器完成对象的序列化
                tea_seria = TeacherSerializer(tea_obj)
                return Response({
                    'status': 200,
                    'message': '查询单个教师成功',
                    'results': tea_seria.data
                }, status=200)
            else:
                return Response({
                    'status': 400,
                    'message': 'id不存在',
                }, status=400)
        else:
            tea_obj_all = Teacher.objects.all()
            #     序列化多个对象时，需要指定属性many=True
            tea_data = TeacherSerializer(tea_obj_all, many=True).data
            return Response({
                'status': 200,
                'message': '查询所有教师成功',
                'results': tea_data
            })

    def post(self, request, *args, **kwargs):

        # 获取前端传递的参数
        request_data = request.data

        # 前端传递的数据进行入库时 需要判断数据的格式是否合法
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                'status': 400,
                'message': '参数有误'
            }, status=400)

        serializer = TeacherDeSerializer(data=request_data)
        if (serializer.is_valid()):
            tea_ser = serializer.save()
            return Response({
                'status': 200,
                'message': 'success',
                'results': TeacherSerializer(tea_ser).data
            }, status=200)
        else:
            return Response({
                'status': 400,
                'message': '教师添加失败',
                'results': serializer.errors
            })

    def delete(self, request, *args, **kwargs):
        # 获取前端传递的参数
        request_data = request.data
        print(request_data)
        # 前端传递的数据进行入库时 需要判断数据的格式是否合法
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                'status': 400,
                'message': '参数有误'
            }, status=400)

        tea_id = request_data.get('id')
        if tea_id:
            tea_obj = Teacher.objects.filter(pk=tea_id).first()
            if tea_obj:
                tea_data = TeacherSerializer(tea_obj).data
                tea_obj.delete()
                return Response({
                    'status': 200,
                    'message': '教师删除成功',
                    'results': tea_data
                },status=200)
            else:
                return Response({
                    'status': 300,
                    'message': '无此id',
                }, status=300)
        else:
            return Response({
                'status': 400,
                'message': '参数有误'
            }, status=400)


