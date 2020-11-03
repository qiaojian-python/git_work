import jwt
from rest_framework import exceptions
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
#
# class JWTAuthentication(BaseJSONWebTokenAuthentication):
#
#     def authenticate(self, request):
# #         获取前端传递的token
#         jwt_token = request.META.get("HTTP_AUTHORIZATION",None)
#         print(jwt_token)


# 自定义校验
from rest_framework_jwt.serializers import jwt_decode_handler


class JWTAuthencation(BaseJSONWebTokenAuthentication):

    def authenticate(self, request):
        # 获取前端传递的token
        jwt_value = request.META.get("HTTP_AUTHORIZATION",  None)
        token = self.parse_jwt_token(jwt_value)
        if token is None:
            return None

    #     将通过token 反解析出载荷
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed("签名过期")
        except:
            raise exceptions.AuthenticationFailed("非法用户")
    #     没有任何异常 解析通过 解析出对象
        user = self.authenticate_credentials(payload)
        return user,token

    # 解析token
    def parse_jwt_token(self, jwt_token):
        tokens = jwt_token.split()

        if len(tokens) != 3 or tokens[0].lower() != 'auth' or tokens[2].lower() != 'jwt':
            return None

        return tokens[1]







