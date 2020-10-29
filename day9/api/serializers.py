from rest_framework import serializers

from api.models import Book, Press


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



# 序列器与反序列器进行整合

class BookModelSerializerV2(serializers.ModelSerializer):

    class Meta:
        model = Book
#         fields应该写序列化与反序列化所需字段的并集
#         反序列('book_name','price','publish','authors')
#         序列('id','book_name','price','pic1','press_name')

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
        print(1234)
        return attrs

    def validated_book_name(self,value):
        print(value)
        return value
