import json
import xml.sax

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from django.utils import timezone

from rest_framework.exceptions import NotFound, ParseError, NotAuthenticated


from dynamic_preferences.registries import global_preferences_registry

from .models import User

from .tools import XMLHandler

# Create your views here.

# 实力话首选项管理器
global_preferences = global_preferences_registry.manager()


class index(View):
    def get(self, request):
        # 测试redis缓存存储数据
        cache.set('foo', 'ojbk', timeout=60)
        c = cache.get('foo')
        return HttpResponse('值为：%s' % c)


class make_expire(View):
    '''
    persist:永不过期
    expire：指定新的过期超时
    '''

    def get(self, request):
        # 将特定的缓存key记性过期操作
        cache.persist('foo')
        c = cache.ttl('foo')
        return HttpResponse('%s' % c)


class get_key(View):
    def get(self, request):
        c = cache.get('foo')
        expire = cache.ttl('foo')
        return HttpResponse('值为：%s，过期时间还剩：%s秒' % (c, expire))


class test_xml(View):
    def get(self, request):
        result = request.body.decode()
        print(result)
        xh = XMLHandler()
        xml.sax.parseString(result, xh)
        ret = xh.getDict()
        print(ret['return_code'])
        # 接收xml数据
        return HttpResponse('ok')


class transition(View):
    def get(self, request):
        xml_data = """<xml>
            <return_code>{return_code}</return_code>
            <result_code>{result_code}</result_code>
            </xml>
        """
        return HttpResponse(xml_data,content_type='text/xml')






class check_user(View):
    def post(self, request):
        name = request.POST.get('name', '')
        if name:
            user = User.diy.get_user(name)
            print(user[0].age)
            # u = User.objects.get_queryset()
            # print(u)
            # uu = User.diy.get_queryset()
            # print(uu)
            # uuu = User.objects.all()
            # print(uuu)
            # uuuu = User.diy.all()
            # print(uuuu)
            uuuuu = User.diythree.create_u('王五', True, 20)
            print(uuuuu.name)
        return HttpResponse('ok')


# 测试全局的首选项
class Test_section(View):
    def post(self, request):
        all_section = global_preferences.all()
        print(all_section)
        # 更新一个全局首选项
        global_preferences['general__title'] = 'tttttttttttt'

        # 获取到全局首选项title的值
        title_value = global_preferences['general__title']
        print(title_value)

        # 获取到未在数据库存在全局首选项
        sex = global_preferences['general__sex']
        print(sex)
        return HttpResponse('ok')

# 查看当前时区信息
class Check_tz(View):
    def get(self,request):
        t=timezone.now()
        print(t)
        return HttpResponse('ok')


# 测试断点
class Test_duandian(View):
    def get(self,request):
        print('开始断点了')
        a
        print('断点结束了')
        return HttpResponse('ok')


# 测试自定义过滤csrf的路由
class Test_csrf(View):
    def post(self,request):
        name = request.POST.get('name')
        return HttpResponse(name)
    

# 测试在视图中出现Falses时,会有啥反应?会报错停止吗?
# 测试获取协议及其域名和段口

class Test_false(View):
    def get(self,request):
        print('进入视图')
        True
        print('从视图出来啦')
        False
        host = '{scheme}://{host}'.format(
                    scheme=request.scheme,
                    host=request.get_host()
                )
        
        # raise ParseError(detail="Charge amount != course money")   # 直接会把错误打印到日志上,返回500服务器错误
        return HttpResponse(host)    
# 结果:   没有报错???
# 进入视图
# 从视图出来啦


# 测试抛出错误,前端是何种显示
class Test_raise(View):
    def get(self,request):
        # raise Exception(detail="Charge amount != course money")
        return HttpResponse('ok')


from django.contrib import messages

# 测试django 模板中messages消息提示
class Test_message(View):
    def get(self,request):
        name = request.GET.get('name',None)
        if not name:
            messages.error(request,'缺少name参数啊')
            return render(request,'index.html')
        return HttpResponse('ok')