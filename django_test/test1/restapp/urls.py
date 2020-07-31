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
from app1 import views


urlpatterns = [
    # url(r"^course/$", views.Test_listview.as_view(), name="Test_listview"),
    # url(r"^test_detailview/(?P<pk>\d+)$", views.Test_detailview.as_view(), name="test_detailview"),
    # url(r"^test_redis/$", views.Test_redis.as_view(), name="test_redis"),
    # url(r"^test_redsi_ex/$", views.Test_redsi_ex.as_view(), name="test_redsi_ex"),
    # url(r"^test_reat_auth/$", views.Test_reat_auth.as_view(), name="test_reat_auth"),

]