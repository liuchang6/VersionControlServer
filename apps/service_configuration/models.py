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

    name = models.CharField(max_length = 50,verbose_name = '名称')
    desc = models.CharField(max_length=2000, blank=True, null=True, verbose_name='描述')
    ip = models.GenericIPAddressField(verbose_name = 'IP地址')
    password = models.CharField(max_length=50, verbose_name='密码')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    delete = models.CharField(max_length = 50,verbose_name = '是否删除：0 已删除；1 未删除',choices=delete_choices)


    class Meta():
        db_table = 'server_info'
        verbose_name = '服务配置信息'


    def __str__(self):
        return self.name