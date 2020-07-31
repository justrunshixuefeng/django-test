from django.db import models

# Create your models here.


class User_manager_two(models.Manager):
    def getzhangsan(self):
        return self.filter(name='张三')


class User_manager(models.Manager):
    def get_user(self, name):
        return self.filter(name=name)

    def get_queryset(self):
        return super().get_queryset().filter(name='张三')


class create_user(models.Manager):
    # 在管理器类中定义创建对象的方法  第一种
    # def create(self, name, sex, age):
    #     u = self.model()  # 创建模型类对象self.model可以获得模型类
    #     u.name = name
    #     u.sex = sex
    #     u.age = age
    #     u.save()
    #     return u
    # 第二种
    def create_u(self, name, sex, age):
        u = self.get_queryset().create(name=name,sex=sex,age=age)
        return u

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    sex = models.BooleanField(verbose_name='性别', default=True)
    age = models.IntegerField(verbose_name='年龄')
    objects = models.Manager()
    diy = User_manager()
    diytwo = User_manager_two()
    diythree = create_user()

    def __str__(self):
        return self.name


class course(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    zuozhe = models.CharField(max_length=100,verbose_name='作者')
    price = models.CharField(max_length=50,verbose_name='价格')

    def __str__(self):
        return self.title
    