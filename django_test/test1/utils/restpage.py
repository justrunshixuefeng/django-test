from rest_framework.pagination import PageNumberPagination

#重写的自定义的分页类，给特例的api使用
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 5 # 每页显示多少条数据
    page_query_param = 'pp' # 127.0.0.1:8000/books/?pp=5 查询第5页
    page_size_query_param = 'page_size' # 提供用户自行控制显示多少条数据，127.0.0.1:8000/books/?page_param=5
    max_page_size = 10000 # 控制上一行每页最多现实多少条