# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 14:58
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : service.py
# @Software: PyCharm

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from version_control.models import ServerInfo
from version_control.serializers import ServerInfoSerializer
from version_control.utils.response import *
from version_control.pagination import MyPageNumberPagination
"""
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
"""
# Create your views here.

class ServerInfoView(ModelViewSet):
    '''
    项目管理
    '''

    queryset = ServerInfo.objects.filter(delete=1)
    serializer_class = ServerInfoSerializer
    pagination_class = MyPageNumberPagination

    def list(self, request):
        """
        所有项目信息
        """
        Servers = self.get_queryset()
        page_Servers = self.paginate_queryset(Servers)
        serializer = self.get_serializer(page_Servers, many=True)
        return self.get_paginated_response(serializer.data)


    def create(self, request):
        """
        创建项目
        """
        name = request.data["name"]
        if ServerInfo.objects.filter(name=name).first():
            SERVICE_EXISTS["name"] = name
            return Response(SERVICE_EXISTS)
        # 反序列化
        serializer = ServerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(PROJECT_ADD_SUCCESS)
        return Response(SYSTEM_ERROR)

    def retrieve(self, request, **kwargs):
        """
        单个项目信息
        """
        pk = kwargs.pop('pk')
        try:
            queryset = ServerInfo.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(PROJECT_NOT_EXISTS)
        serializer = self.get_serializer(queryset, many=False)
        BASE['data'] = serializer.data
        return Response(BASE)





