from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    """
    用户表
    """

    class Meta:
        db_table = "tb_user"
        verbose_name = "用户配置"

    def __str__(self):
        return self.username

class ServerInfo(models.Model):
    """
    服务器信息
    """
    delete_choices = (
        (0, "已删除"),
        (1, "未删除"),
    )
    status_choices = (
        (0, "无法连接"),
        (1, "连接正常"),
    )

    name = models.CharField(max_length = 50,verbose_name = '名称')
    desc = models.CharField(max_length=2000, blank=True, null=True, verbose_name='描述')
    port = models.CharField(max_length=10, verbose_name='端口')
    user = models.CharField(max_length=50, verbose_name='用户名')
    ip = models.GenericIPAddressField(verbose_name = 'IP地址')
    password = models.CharField(max_length=50, verbose_name='密码')
    status = models.CharField(max_length=1, verbose_name='状态',choices=status_choices,default=1)
    creater = models.CharField(max_length=50, verbose_name='创建人')
    check_time = models.DateTimeField(verbose_name='上次检测时间', auto_now_add=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now_add=True)
    delete = models.CharField(max_length = 1,verbose_name = '是否删除',choices=delete_choices,default=1)

    class Meta():
        db_table = 'tb_server_info'
        verbose_name = '服务器配置'

    def __str__(self):
        return self.name


class RepositoryInfo(models.Model):
    """
    代码仓库信息
    """
    delete_choices = (
        (0, "已删除"),
        (1, "未删除"),
    )
    status_choices = (
        (0, "无法连接"),
        (1, "连接正常"),
    )

    name = models.CharField(max_length = 50,verbose_name = '名称')
    desc = models.CharField(max_length=2000, blank=True, null=True, verbose_name='描述')
    url = models.CharField(max_length = 255,verbose_name='仓库地址')
    user = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=50, verbose_name='密码')
    branches = models.CharField(max_length=500, verbose_name='代码分支')
    status = models.CharField(max_length=1, verbose_name='状态',choices=status_choices,default=1)
    creater = models.CharField(max_length=50, verbose_name='创建人')
    check_time = models.DateTimeField(verbose_name='上次检测时间', auto_now_add=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now_add=True)
    delete = models.CharField(max_length = 1,verbose_name = '是否删除',choices=delete_choices,default=1)

    class Meta():
        db_table = 'tb_repository_info'
        verbose_name = '代码仓库配置'

    def __str__(self):
        return self.name