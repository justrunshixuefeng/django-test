from django.contrib.auth.models import User, Group

from rest_framework import serializers

from restapp.models import UserInformation

# HyperlinkedModelSerializer   超链接模型的序列化器


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        # fields = '__all__'
        exclude = ['owner']

