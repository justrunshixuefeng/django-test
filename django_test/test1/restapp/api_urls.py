from django.conf.urls import url,include

from restapp import views,api
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'testviewsets', api.Test_ModelViewSet)

urlpatterns = [

    # API 接口

    url(r'^', include(router.urls)),
]