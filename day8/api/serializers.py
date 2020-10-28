
# 定义序列器
from rest_framework import serializers

from api.models import Employee, Teacher
from drf_day2 import settings


class EmployeeSerializer(serializers.Serializer):
    """
    需要为每个model编写对应的序列化器类
    """
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    phone = serializers.CharField()
    # pic = serializers.ImageField()

    aaa = serializers.SerializerMethodField()

    def get_aaa(self, obj):
        # print(type(obj))
        return 'aaa'

    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        # print(obj.get_gender_display())
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        print(obj.pic)
        return "%s%s%s" % ('http://127.0.0.1:8000/',settings.MEDIA_URL,str(obj.pic))


# 反序列化器定义

class EmployeeDeSerializer(serializers.Serializer):
    # 添加校验规则
    username = serializers.CharField(
        max_length=6,
        min_length=2,
        error_messages={
            'max_length':'too long',
            'min_length':'too short',
        }
    )
    password =serializers.CharField()
    phone = serializers.CharField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)





class TeacherSerializer(serializers.Serializer):
    """
    需要为每个model编写对应的序列化器类
    """
    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()
    school = serializers.CharField()
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        print(obj.get_gender_display())
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        print(obj.pic)
        return "%s%s%s" % ('http://127.0.0.1:8000/',settings.MEDIA_URL,str(obj.pic))


# 反序列化器定义

class TeacherDeSerializer(serializers.Serializer):
    # 添加校验规则
    username = serializers.CharField(
        max_length=6,
        min_length=2,
        error_messages={
            'max_length':'too long',
            'min_length':'too short',
        }
    )
    password =serializers.CharField()
    phone = serializers.CharField()
    school = serializers.CharField()
    gender = serializers.IntegerField()

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)


