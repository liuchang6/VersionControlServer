# Generated by Django 3.0.2 on 2020-01-31 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0005_auto_20200129_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepositoryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('desc', models.CharField(blank=True, max_length=2000, null=True, verbose_name='描述')),
                ('url', models.GenericIPAddressField(verbose_name='仓库地址')),
                ('user', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('status', models.CharField(choices=[(0, '无法连接'), (1, '连接正常')], default=1, max_length=1, verbose_name='状态')),
                ('creater', models.CharField(max_length=50, verbose_name='创建人')),
                ('check_time', models.DateTimeField(auto_now_add=True, verbose_name='上次检测时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('delete', models.CharField(choices=[(0, '已删除'), (1, '未删除')], default=1, max_length=1, verbose_name='是否删除')),
            ],
            options={
                'verbose_name': '代码仓库配置',
                'db_table': 'tb_repository_info',
            },
        ),
        migrations.AlterModelOptions(
            name='serverinfo',
            options={'verbose_name': '服务器配置'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户配置'},
        ),
    ]
