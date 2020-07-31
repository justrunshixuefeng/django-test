import hashlib

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from authpermis import serializer

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from authpermis import models
from authpermis.utils.permission import SVIPPermission, NosvipPermission, Check_student_Permission, Update_age_Permission
from utils import utils

# Create your views here.

# class CourseViewSet(viewsets.ModelViewSet):
#     def get_permissions(self):


class OrderView(View):
    """
    订单相关业务(只有SVIP用户有权限)

    是否是应用了restful框架的认证系统,所以request.user可以获取到当前用户呢?还是本来就可以获取到用户的?
    估计是用了restful框架,所以在请求通过认证系统时,将用户封装在了request中
    """
    # 添加自定义的权限
    permission_classes = [NosvipPermission, ]

    def get(self, request, *args, **kwargs):
        # request.user
        # request.auth
        # self.dispatchdispatch
        result = request.user
        print('request.user值为:%s' % result)
        # permis = request.user.user_type
        # print('当前登陆用户的等级为:%s'%permis)
        # auth = request.auth
        # print(type(auth))
        # print('认证信息为:%s' % auth)
        # if request.user.user_type != 3:
        #     return HttpResponse("无权访问")

        ret = {'code': 1000, 'msg': None, 'data': None}
        try:
            ret['data'] = '十包辣条'
        except Exception as e:
            pass
        return JsonResponse(ret)


class AuthView(APIView):
    """
    用于用户登录认证
    """
    authentication_classes = []

    def post(self, request, *args, **kwargs):

        ret = {'code': 1000, 'msg': None}
        # try:

        user = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = models.UserInfo.objects.filter(
            username=user, password=pwd).first()
        if not obj:
            ret['code'] = 1001
            ret['msg'] = "用户名或密码错误"
        # 为登录用户创建token
        token = utils.get_md5(user)
        # 存在就更新，不存在就创建
        models.UserToken.objects.update_or_create(
            user=obj, defaults={'token': token})
        ret['token'] = token

        # except Exception as e:
        #     ret['code'] = 1002
        #     ret['msg'] = '请求异常'

        return JsonResponse(ret)


class All_student(APIView):
    '''
    只有老师可以调用此接口
    '''
    permission_classes = [Check_student_Permission]

    def get(self, request):
        students = models.Student.objects.all()
        stus = serializer.Studentserializer(instance=students, many=True)
        return Response(stus.data)


# 修改学生的年龄,老师可以调用此接口,但是只有学生的老师可以修改
class Update_student(APIView):
    '''
    获取到学生的的id和要更改的年龄
    '''
    permission_classes = [Update_age_Permission]

    def post(self, request):
        id = request.POST.get('id')
        age = request.POST.get('age')
        # 获取到学生的信息
        stu = models.Student.objects.get(pk=id)
        stu.age = age
        stu.save()
        self.check_object_permissions(request, stu)
        # return Response({'code': 200, '学生年龄修改为': stu.age})
        stu = serializer.Studentserializer(data=stu)
        return Response(stu)


# 测试jwt认证
# class Test_jwt_token(APIView):
#     '''
#     '''
#     def get(self,requst):






# 测试刷新jwt token