# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 18:29
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from version_control.models import ServerInfo,UserInfo,RepositoryInfo

class UserInfoSerializer(serializers.ModelSerializer):
    """
    用户信息序列化
    """
    class Meta:
        model = UserInfo
        fields = ['username', 'password']

class ServerInfoSerializer(serializers.ModelSerializer):
    """
    服务信息序列化
    """
    status = serializers.CharField( read_only=True)
    password = serializers.CharField(required=True,write_only=True)
    creater = serializers.CharField(required=False)
    check_time = serializers.DateTimeField( read_only=True,format='%Y-%m-%d %H:%M:%S', required=False)
    update_time = serializers.DateTimeField( format='%Y-%m-%d %H:%M:%S', required=False)
    create_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = ServerInfo
        exclude = ['delete']

class ConnectServerInfoSerializer(serializers.ModelSerializer):
    """
    服务信息获取密码序列化
    """
    class Meta:
            model = ServerInfo
            fields = ['name','password','user','ip','port','desc']

class RepositoryInfoSerializer(serializers.ModelSerializer):
    """
    代码仓库信息序列化
    """
    status = serializers.CharField( read_only=True)
    password = serializers.CharField(required=True,write_only=True)
    creater = serializers.CharField(required=False)
    check_time = serializers.DateTimeField( read_only=True, format='%Y-%m-%d %H:%M:%S', required=False)
    update_time = serializers.DateTimeField( format='%Y-%m-%d %H:%M:%S', required=False)
    create_time = serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M:%S', required=False)
    class Meta:
        model = RepositoryInfo
        exclude = ['delete']

class ConnectRepositoryInfoSerializer(serializers.ModelSerializer):
    """
    代码仓库获取密码信息序列化
    """
    class Meta:
            model = RepositoryInfo
            fields = ['name','password','user','url','desc']