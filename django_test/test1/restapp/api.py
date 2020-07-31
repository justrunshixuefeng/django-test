from rest_framework import viewsets
from rest_framework.response import Response

from restapp.serializers import UserInformationSerializer
from restapp.models import UserInformation

from utils.restpage import StandardResultsSetPagination,LargeResultsSetPagination


# 测试viewsets.ModelViewSet的各项功能
class Test_ModelViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer
    permission_classes = []
    # pagination_class = StandardResultsSetPagination
    pagination_class = LargeResultsSetPagination

    def list(self, request, *args, **kwargs):
        '''
        请求:http://127.0.0.1:8000/restapps/testviewsets/ 得到如下结果
        '{"count":4,
        "next":"http://127.0.0.1:8000/restapps/testviewsets/?page=2",
        "previous":null,
        "results":[
            {"id":1,"name":"admin大哥","age":30,"passwd":"123456"},
            {"id":2,"name":"shixf大哥","age":30,"passwd":"123456"},
            {"id":3,"name":"阿龙大哥","age":30,"passwd":"123456"},
            {"id":4,"name":"阿迪大哥","age":30,"passwd":"123456"}
        ]}'
        '''
        # position = request.query_params.get("position")

        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserInformationSerializer(queryset, many=True)
        page = self.paginate_queryset(queryset)
        data_list = serializer.data
        return self.get_paginated_response(data_list)
        if page is not None:
            data_list = serializer.data
            # 为给定的输出数据返回分页样式的Response对象
            return self.get_paginated_response(data_list)
        return Response(serializer.data)
