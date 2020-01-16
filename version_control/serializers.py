# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 18:29
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from version_control.models import ServerInfo


class ServerInfoSerializer(serializers.ModelSerializer):
    """
    服务信息序列化
    """
    status = serializers.CharField( read_only=True)
    password = serializers.CharField(required=True,write_only=True)
    check_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S', required=False)
    update_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S', required=False)
    create_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = ServerInfo
        exclude  = ['delete']

