# 自定义签发token序列化器
import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.settings import api_settings

from api.models import User, Computer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
class UserModelSerializer(ModelSerializer):
    """
    前端发送请求 传递参数 但数据不需要保存至数据库  只校验
    # 反序列化过程中 有些字段只参与反序列化的业务 ，并不会保存到数据中， 模型也没有对应的字段
    """
    # 自定义反序列化字段 只参与反序列化  不进行model类映射
    account = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['account','password','username','phone','email']

        extra_kwargs = {
            "username":{
                "read_only": True
            },
            "phone": {
                "read_only": True
            },
            "email": {
                "read_only": True
            },
        }

    def validate(self, attrs):
        account = attrs.get('account')
        password = attrs.get('password')
        # 对各种登录方式做处理 账号 邮箱  手机号
        if re.match(r'1[3-9][0-9]{9}', account):
            user_obj = User.objects.filter(phone=account).first()
        elif re.match(r'.+@.+', account):
            user_obj = User.objects.filter(email=account).first()
        else:
            user_obj = User.objects.filter(username=account).first()
        # 判断用户是否存在  check_password解密验证
        if user_obj and user_obj.check_password(password):
        #     成功签发token
            """
            根据用户信息生成载荷
            根据载荷生成token
            
            """
            payload =jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            # 将用户和token给视图
            self.obj = user_obj
            self.token = token
        return attrs



# 电脑序列化器
class ComputerModelSerializer(ModelSerializer):

    class Meta:
        model = Computer
        fields = ('name','price','brand')

