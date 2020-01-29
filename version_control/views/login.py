# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 11:28
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : login.py
# @Software: PyCharm

from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.serializers import jwt_encode_handler
from django.contrib import auth

class LoginView(ModelViewSet):
    queryset = ServerInfo.objects.filter(
        delete=1).order_by(
        '-create_time',
        '-update_time')
    filter_class = ServerFilter
    filter_fields = ("name", "ip")
    serializer_class = ServerInfoSerializer
    pagination_class = MyPageNumberPagination
    def create(self, request, *args, **kwargs):
        pass