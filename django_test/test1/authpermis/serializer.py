from rest_framework.serializers import ModelSerializer
from authpermis.models import User, Student


# 用户表序列化器
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



# 学生表序列化器
class Studentserializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('name', 'age')
