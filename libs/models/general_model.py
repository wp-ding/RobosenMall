from django.db import models


# 用户基础表
class User_Base(models.Model):
    NATION_CHOICES = {
        1: '中国',
        2: '海外',
    }
    AUTH_CHOICES = {
        0: '已启用',
        1: '已禁用',
    }

    user_id = models.CharField(
        primary_key=True,
        max_length=50,
        verbose_name='用户编号',
    )
    username = models.CharField(
        max_length=50,
        verbose_name='用户名',
    )

    phone = models.CharField(
        max_length=25,
        verbose_name='手机号'
    )
    email = models.EmailField(
        null=True,
        verbose_name='邮箱'
    )
    password = models.CharField(
        max_length=255,
        verbose_name='密码'
    )
    nation = models.IntegerField(
        default=1,
        choices=NATION_CHOICES.items(),
        verbose_name='国籍'
    )
    icon_url = models.CharField(
        null=True,
        max_length=255,
        verbose_name='个人头像'
    )
    last_login_time = models.DateTimeField(
        auto_now=True,
        verbose_name='上次登录时间'
    )
    regist_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='注册时间',
    )
    user_status = models.IntegerField(
        default=0,
        choices=AUTH_CHOICES.items(),
        verbose_name='用户状态'
    )
    ext_id = models.CharField(
        max_length=50,
        null=True,
        verbose_name='三方关联账号编号'
    )
    written_off = models.BooleanField(
        default=False,
        verbose_name='注销状态'
    )

    class Meta:
        verbose_name = '用户基础信息表'
        verbose_name_plural = verbose_name
        db_table = 'User_Base'