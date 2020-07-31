import time

from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.http import Http404, HttpResponse
from django.views import View
from django.contrib.auth.models import User, Group

# from app1.models import User, course

from restapp.utils import redis
from restapp.serializers import UserSerializer, GroupSerializer, UserInformationSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from restapp.models import UserInformation
# Create your views here.


# class Test_listview(ListView):
#     '''
#     测试各种view
#     '''

#     # 使用哪一个模板
#     template_name = 'index.html'
#     # 给模板返回的变量名字
#     context_object_name = 'obj_list'

#     def get_queryset(self):
#         obj = course.objects.filter(zuozhe='张三')
#         return obj

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         ticks = [i for i in range(3)]
#         context['now'] = ticks  # 只有这行代码有用
#         print(context['now'])
#         return context


# class Test_detailview(DetailView):
#     '''
#     测试Detailview的方法
#     '''
#     queryset = course.objects.all()
#     template_name = 'index.html'
#     context_object_name = 'obj_list'

#     def get_object(self, **kwargs):
#         # 获取到传来的参数,将符合作者的书全部找出来
#         pass


# class Test_redis(View):
#     '''
#     测试redis存储及过期时间
#     '''

#     def get(self, request):
#         redis.set('nihao', 'haohaohao', ex=10)
#         a = redis.get('nihao')
#         print(a)
#         b = redis.get('caocao')
#         print('bbbbbb')
#         print(b)
#         c = redis.set('no_value', 'True', ex=10)
#         return HttpResponse(a)


# class Test_redsi_ex(View):
#     '''
#     测试redsi的过期时间
#     '''

#     def get(self, request):
#         a = redis.get('nihao')
#         c = redis.get('no_value')
#         print(c+c+c+c+c)
#         return HttpResponse(a, c)


# # 测试rest认证
# class Test_reat_auth(APIView):
#     '''
#     测试两点:
#     1.查看到用户是否是登陆用户
#     2.认证过得用户才可以获取到此接口的响应
#     '''

#     def post(self, request):
#         user = request.user
#         print(user)
#         name = user.username
#         # flname = user.get_full_name()
#         print(name)
#         # print(flname)
#         if user:
#             return Response({'mes': '当前登陆用户为:%s' % user.username})
#         else:
#             return Response({'mes': '当前用户为游客'})


'''
我们不是编写多个视图，而是将所有常见的行为组合到一个名为viewset的类中。

如果需要的话，我们可以很容易地将它们分解为单独的视图，但是使用viewset使视图逻辑组织得很好，并且非常简洁。
'''


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    允许查看或编辑用户的API端点。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    允许查看或编辑组的API端点。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer





