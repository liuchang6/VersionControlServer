# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 17:58
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : repository.py
# @Software: PyCharm
import datetime
import base64

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status,mixins,filters
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.response import Response

from version_control.utils.response import *
from version_control.models import RepositoryInfo
from version_control.utils.jwt_auth import JWTAuthentication
from version_control.utils.git_tool import GitRepository
from version_control.pagination import MyPageNumberPagination
from version_control.serializers import RepositoryInfoSerializer,ConnectRepositoryInfoSerializer


"""
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
"""


# Create your views here.

class RepositoryInfoView(ModelViewSet):
    '''
    代码仓库管理
    '''

    queryset = RepositoryInfo.objects.filter(
        delete=1).order_by(
        '-create_time',
        '-update_time')
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    serializer_class = RepositoryInfoSerializer
    pagination_class = MyPageNumberPagination
    authentication_classes = (JWTAuthentication,)
    permissions_classes = ()

    def list(self, request):
        """
        所有代码仓库信息
        """
        Repository = self.get_queryset()
        page_Repository = self.paginate_queryset(Repository)
        serializer = self.get_serializer(page_Repository, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        """
        创建代码仓库
        """
        name = request.data["name"]
        if RepositoryInfo.objects.filter(name=name).first():
            NAME_EXISTS["name"] = name
            return Response(NAME_EXISTS)
        serializer = RepositoryInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(ADD_SUCCESS)
        SYSTEM_ERROR['msg'] = serializer.errors
        return Response(SYSTEM_ERROR)

    def retrieve(self, request, **kwargs):
        """
        单个服务信息
        """
        pk = kwargs.pop('pk')
        try:
            queryset = RepositoryInfo.objects.filter(
        delete=1).get(id=pk)
        except ObjectDoesNotExist:
            return Response(NAME_NOT_EXISTS)
        serializer = self.get_serializer(queryset, many=False)
        BASE['data'] = serializer.data
        return Response(BASE)

    def update(self,request, **kwargs):
        pk = kwargs.pop('pk')
        queryset = RepositoryInfo.objects.get(id=pk)
        request.data['update_time'] = datetime.datetime.now()
        serializer = RepositoryInfoSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(UPDATE_SUCCESS)
        SYSTEM_ERROR['msg'] = serializer.errors
        return Response(SYSTEM_ERROR)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        try:
            RepositoryInfo.objects.filter(id=pk).update(**{'delete':'0'})
        except ObjectDoesNotExist:
            return Response(NAME_NOT_EXISTS)
        return Response(DELETE_SUCCESS)



class ConnectRepositoryInfoView(GenericViewSet,mixins.RetrieveModelMixin):
    """
    连接服务器信息
    """
    queryset = RepositoryInfo.objects.filter(
        delete=1)
    serializer_class = ConnectRepositoryInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        try:
            queryset = RepositoryInfo.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(NAME_NOT_EXISTS)
        serializer = self.get_serializer(queryset, many=False)
        password = base64.b64encode(serializer.data['password'].encode())
        BASE['data'] = serializer.data
        BASE['data']['password'] = password
        return Response(BASE)

class CheckRepositoryView(GenericViewSet,mixins.CreateModelMixin):
    """
    服务信息
    """
    queryset = RepositoryInfo.objects.filter(
        delete=1)
    serializer_class = RepositoryInfoSerializer

    def create(self, request):
        """
        单个服务信息
        """
        data=request.data
        user = data['user']
        passwd = data['password']
        url = data['url']

        git = GitRepository(user, passwd, url,settings.LOCAL_GIT_REPOSITORY_PATH)
        result = git.get_branch()

        if result == 'AuthenticationFailed':
            return Response(AUTHENTICATION_FAILED,status.HTTP_200_OK)
        elif result == 'TimeOut':
            return Response(TIME_OUT_ERROR,status.HTTP_200_OK)
        else:
            return Response(CHECK_OK, status.HTTP_200_OK)
        return Response(SYSTEM_ERROR)