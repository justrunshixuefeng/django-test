from rest_framework.permissions import BasePermission

#  校验 SVIP 用户 才能访问的验证


class SVIPPermission(BasePermission):
    message = "必须是SVIP才能访问"

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False
        return True

# 除了 SVIP用户都可以访问的验证


class NosvipPermission(BasePermission):
    message = '你没有权限去执行这个动作!!!'

    def has_permission(self, request, view):
        if request.user.user_type == 3:
            return False
        return True

# 只有老师可以查看所有学生的信息


class Check_student_Permission(BasePermission):
    message = '你不是老师,无权查看学生信息'

    def has_permission(self, request, view):
        print(request.user)
        user_type = request.user.type
        print('当前用户的类型为:%s' % str(user_type))
        if user_type == 1:
            return False
        if user_type == 2:
            return True
        return False


# 老师可以查看学生,但是老师只能更改自己学生的信息
class Update_age_Permission(BasePermission):
    message = '你不是此学生的老师,乱改啥?'

    def has_permission(self, request, view):
        if request.user.type == 1:
            return False
        if request.user.type == 2:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # 老师的id
        teacher_id = request.user.id
        print('老师id为:%s' % teacher_id)
        print('学生所属老师id:%s' % obj.teacher_id)
        # 如果老师的id和学生所属老师id不一致
        if obj.teacher_id != teacher_id:
            return False
        return True
