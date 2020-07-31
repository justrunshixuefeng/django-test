"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import app1
from restapp.views import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from restapp import views

# 测试rest需要
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^restapp/', include('restapp.urls')),
    url(r'^learnapp/', include('learnapp.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^authpermis/', include('authpermis.urls')),

    url(r'^restapps/',include('restapp.api_urls')),

    # jwt认证
    url(r'^', include(router.urls)),
    # 如果您打算使用可浏览的API，您可能还需要添加REST框架的登录和注销视图。将以下内容添加到您的根urls.py文件中。    可浏览API的登录url
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^auth/$', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),

    url(r'^admin/', admin.site.urls),
    url(r'^index/$', app1.views.index.as_view(), name='index'),
    url(r'^make_expire/$', app1.views.make_expire.as_view(), name='make_expire'),
    url(r'^get_key/$', app1.views.get_key.as_view(), name='get_key'),
    url(r'^test_xml/$', app1.views.test_xml.as_view(), name='test_xml'),
    url(r'^transition/$', app1.views.transition.as_view(), name='transition'),
    url(r'^check_user/$', app1.views.check_user.as_view(), name='check_user'),
    url(r'^test_section/$', app1.views.Test_section.as_view(), name='test_section'),
    url(r'^check_tz/$', app1.views.Check_tz.as_view(), name='check_tz'),
    url(r'^test_duandian/$', app1.views.Test_duandian.as_view(), name='test_duandian'),
    url(r'^test_csrf/$', app1.views.Test_csrf.as_view(), name='test_csrf'),
    url(r'^test_false/$', app1.views.Test_false.as_view(), name='test_false'),
    url(r'^test_raise/$', app1.views.Test_raise.as_view(), name='test_raise'),
    # 测试TemplateView,会返回啥东西,返回的就是html,并不需要view视图
    url(r'^charge/$', TemplateView.as_view(template_name="charge.html"), name="charge"),
    url(r'^test_message/$', app1.views.Test_message.as_view(), name='test_message'),

]
