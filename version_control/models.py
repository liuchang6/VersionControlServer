from django.db import models

# Create your models here.


class ServerInfo(models.Model):
    """
    配置信息
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
    check_time = models.DateTimeField('上次检测时间', auto_now_add=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    delete = models.CharField(max_length = 1,verbose_name = '是否删除',choices=delete_choices,default=1)

    class Meta():
        db_table = 'server_info'
        verbose_name = '服务配置信息'

    def __str__(self):
        return self.name