# -*- coding: utf-8 -*-
# @Time    : 2020/1/1 11:28
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : login.py
# @Software: PyCharm

import jwt
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.serializers import jwt_payload_handler,jwt_encode_handler

from version_control.utils.response import AUTHENTICATION_FAILED
from version_control.models import UserInfo

class LoginView(GenericViewSet,CreateModelMixin):
    authentication_classes = ()
    permission_classes = ()
    queryset = UserInfo.objects.all()

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        try:
            user = UserInfo.objects.get(username=username)
        except:
            return Response(AUTHENTICATION_FAILED)

        if password != user.password:
            return Response( AUTHENTICATION_FAILED)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            'user': user.last_name+user.first_name,
            'success': True,
            'token': token
        })


class CheckTokenView(GenericViewSet,CreateModelMixin):
    authentication_classes = ()
    permission_classes = ()
    queryset = UserInfo.objects.all()

    def create(self, request, *args, **kwargs):
        token = request.data['token']
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            return Response({ 'ok': False,'msg':'token过期'})
        except:
            return Response({ 'ok': False,'msg':'token非法'})
        return Response({
            'ok': True,
        })