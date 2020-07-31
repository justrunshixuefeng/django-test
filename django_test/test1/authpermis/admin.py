from django.contrib import admin
from authpermis import models

# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.UserToken)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.User)
