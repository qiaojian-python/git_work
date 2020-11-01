from rest_framework import serializers, exceptions

from api.models import Book, Press, TUser


# 出版社序列化器
class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ('press_name', 'pic', 'address')


class BookModelSerializer(serializers.ModelSerializer):

    # 指定另一个序列化器
    # publish = PressModelSerializer()
    class Meta:
        model = Book
        fields = ('id','book_name','price','pic1','press_name')
        # fields = ('id','book_name','price','pic1','press_name','author_list','publish')
        #  显示的是数据库所有的字段
        # fields = "__all__"
        # exclude = ('is_delete','status','create_time')
        # depth = 1


# 反序列化器
class BookModelDeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('book_name','price','publish','authors')

        # 添加drf提供的默认校检规则
        extra_kwargs = {
            "book_name": {
                "required": True,  # 必填字段
                "min_length": 2,    # 最小长度
            #     错误信息
                "error_messages":{
                    "required":"图书名必须提供",
                    "min_length":'图书名长度不能低于2个字符',
                }
            },

        }

    # 全局钩子
    def validate(self, attrs):
        print(attrs)
        return attrs

#     局部钩子
    def validate_book_name(self, value):
        print(value,222)
        return value


# 群体序列化器
# class BookListSerializer(serializers.ListSerializer):
#     #  重写 update方法
#     def update(self, instance, validated_data):
#     #     要修改的实例对象列表 instance
#     #     要修改的的实例的值列表 validated_data
#         for index, obj in enumerate(instance):
#             self.child.update(obj,validated_data[index])
#         return instance

class BookListSerializer(serializers.ListSerializer):
#     重写update方法
    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        for index, obj in enumerate(instance):
            self.child.update(obj,validated_data[index])
        return instance



# 序列器与反序列器进行整合

class BookModelSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Book
#         fields应该写序列化与反序列化所需字段的并集
#         反序列('book_name','price','publish','authors')
#         序列('id','book_name','price','pic1','press_name')
#         list_serializer_class = BookListSerializer
        list_serializer_class =BookListSerializer
        fields = ('id','book_name','price','publish','authors','pic1','press_name')


        # 添加drf提供的默认校检规则
        extra_kwargs = {
            "book_name": {
                "required": True,  # 必填字段
                "min_length": 2,  # 最小长度
                #     错误信息
                "error_messages": {
                    "required": "图书名必须提供",
                    "min_length": '图书名长度不能低于2个字符',
                }
            },
            #id只读，publish只写，pic1只读，press_name只读，authors只写
            "id":{
                "read_only":True
            },
            "publish": {
                "write_only": True
            },
            "pic1": {
                "read_only": True
            },
            "press_name": {
                "read_only": True
            },
            "authors": {
                "write_only": True
            },

        }
#         钩子函数同样可以用
    def validate(self, attrs):
        # print(1234)
        return attrs

    def validate_book_name(self,value):
        # print(value)
        return value


# 作业序列化器
class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TUser
#         fields应该写序列化与反序列化所需字段的并集

        fields = ('id','username','password','age','phone')
        # re_pwd = serializers.CharField()
        # 添加drf提供的默认校检规则
        extra_kwargs = {
            "username": {
                "required": True,  # 必填字段
                "min_length": 2,  # 最小长度
                "max_length":10, # 最长长度
                # "unique":True, # 必须唯一
                #     错误信息
                "error_messages": {
                    "required": "用户名必须提供",
                    "unique": "用户名重复",
                    "min_length": '用户名长度不能低于2个字符',
                    "max_length": '用户名长度不能多于2个字符',
                }
            },
            "password": {
                "required": True,  # 必填字段
                "min_length": 6,  # 最小长度
                "max_length": 20,  # 最长长度
                #     错误信息
                "error_messages": {
                    "required": "密码必须提供",
                    "min_length": '密码长度不能低于6个字符',
                    "max_length": '密码长度不能多于20个字符',

                },
                "write_only": True
            },
            "age": {
                "required": False,  # 不必填字段
            },
            "phone": {
                "required": False,  # 不必填字段
                "min_length": 11,  # 最小长度
                "max_length": 11,  # 最长长度
                "error_messages": {
                    "min_length": '电话长度为11位',
                    "max_length": '电话长度为11位',
                }
            },
            #id只读，publish只写，pic1只读，press_name只读，authors只写
            "id":{
                "read_only":True
            },



        }
#         钩子函数同样可以用
    def validate(self, attrs):
        # 验证两次密码是否一致
        print(attrs,111)
        # pwd = attrs.get("password")
        # re_pwd = attrs.pop("re_pwd")
        #
        # # 自定义规则  两次密码不一致则不能创建用户
        # if pwd != re_pwd:
        #     raise exceptions.ValidationError("两次密码不一致")
        return attrs

    def validate_username(self,value):
        return value
