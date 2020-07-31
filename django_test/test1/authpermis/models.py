from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserInfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)


class UserToken(models.Model):
    user = models.OneToOneField(to='User')
    token = models.CharField(max_length=64)


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name='老师姓名')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='用户名字')
    user_type = (
        (1, '普通用户'),
        (2, '老师')
    )
    type = models.IntegerField(choices=user_type, verbose_name='用户类型')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='学生姓名')
    age = models.IntegerField(verbose_name='年龄')
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.name

