# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 14:58
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : service.py
# @Software: PyCharm

import base64

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework import  mixins
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.response import Response

from version_control.models import ServerInfo
from version_control.serializers import ServerInfoSerializer,ConnectServerInfoSerializer
from version_control.utils.response import *
from version_control.utils.ssh_tool import CheckSSH
from version_control.pagination import MyPageNumberPagination


"""
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
"""


# Create your views here.

class ServerInfoView(ModelViewSet):
    '''
    服务管理
    '''

    queryset = ServerInfo.objects.filter(
        delete=1).order_by(
        '-create_time',
        '-update_time')
    serializer_class = ServerInfoSerializer
    pagination_class = MyPageNumberPagination

    def list(self, request):
        """
        所有服务信息
        """
        Servers = self.get_queryset()
        page_Servers = self.paginate_queryset(Servers)
        serializer = self.get_serializer(page_Servers, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        """
        创建服务
        """

        name = request.data["name"]
        if ServerInfo.objects.filter(name=name).first():
            SERVICE_EXISTS["name"] = name
            return Response(SERVICE_EXISTS)
        serializer = ServerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(SERVICE_ADD_SUCCESS)

        return Response(SYSTEM_ERROR)

    def retrieve(self, request, **kwargs):
        """
        单个服务信息
        """
        pk = kwargs.pop('pk')
        try:
            queryset = ServerInfo.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(SERVICE_NOT_EXISTS)
        serializer = self.get_serializer(queryset, many=False)
        BASE['data'] = serializer.data
        return Response(BASE)


class ConnectServiceInfoView(GenericViewSet,mixins.RetrieveModelMixin):
    """
    连接服务器信息
    """
    queryset = ServerInfo.objects.filter(
        delete=1)
    serializer_class = ConnectServerInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        try:
            queryset = ServerInfo.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(SERVICE_NOT_EXISTS)
        serializer = self.get_serializer(queryset, many=False)
        password = base64.b64encode(serializer.data['password'].encode())
        BASE['data'] = serializer.data
        BASE['data']['password'] = password
        return Response(BASE)

class CheckServiceView(GenericViewSet,mixins.CreateModelMixin):
    """
    服务信息
    """
    queryset = ServerInfo.objects.filter(
        delete=1)
    serializer_class = ServerInfoSerializer

    def create(self, request):
        """
        单个服务信息
        """
        data=request.data
        user = data['user']
        passwd = data['password']
        ip = data['ip']
        port = data['port']
        print(user,passwd,ip,port)
        ssh = CheckSSH(ip, port, user,passwd)
        print(ssh.sshConnect())
        if not ssh.sshConnect():
            return Response(AUTHENTICATION_FAILED,status.HTTP_200_OK)
        else:
            return Response(SERVER_CHECK_OK, status.HTTP_200_OK)