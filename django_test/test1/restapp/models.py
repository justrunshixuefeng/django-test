from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 测试django 自带的user模型类,能否使用jwt

# 自己生成的token返回给前端其实返回的也是 django自带的user模型啊

class UserInformation(models.Model):
    owner = models.OneToOneField(User, related_name='owner', null=True)
    name = models.CharField(max_length=30, verbose_name=u'姓名', default='')
    age = models.IntegerField(null=True, default=30,
                              blank=True, verbose_name='年龄')
    passwd = models.CharField(
        max_length=100, default='', null=True, verbose_name='密码')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'userInformation'
