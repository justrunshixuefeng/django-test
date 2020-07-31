from rest_framework import exceptions
from authpermis import models
from rest_framework.authentication import BaseAuthentication


class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('token')
        if token == None:
            token = request.POST.get('token')
        print(token)
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest framework内部会将整个两个字段赋值给request，以供后续操作使用
        # 第一个参数是当前用户的记录,第二个参数是用户的验证记录
        # return ('用户记录','用户认证记录')
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        return 'Basic realm="api" 认证失败返回给浏览器的请求头'

