# from rest_framework.response import Response
# from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
# from rest_framework import serializers
#
# def exception_handler(exc, contenxt):
#     print(exc)
#     print(contenxt)
#
#     response = drf_exception_handler(exc, contenxt)
#
#     if response is None:
#         return Response({'error_message':"lll"})
#
# #     处理不了异常
#     return response


# 自定义异常
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc,context):
    error = "%s%s%s" % (context['view'], context['request'].method, exc)
    print(error)

#     先让drf处理异常
    response = drf_exception_handler(exc, context)

#     如果返回值为None，代表drf无法处理此异常 需要自定义处理
    if response is None:
        return Response({
            'error_message':'处理错误中',
        },status=500)
    return response



