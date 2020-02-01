# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 10:22
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : jwt_auth.py
# @Software: PyCharm

import jwt
from rest_framework.exceptions import NotAuthenticated
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.authentication import jwt_decode_handler

class JWTAuthentication(BaseJSONWebTokenAuthentication):
    # 自定义认证类，重写authenticate方法

    def authenticate(self, request):
        # 认证通过，返回user，auth
        # 认证失败，返回None
        auth = request.META.get('HTTP_AUTHORIZATION')
        if not auth:
            return None
        self.key = auth
        try:
            payload = jwt_decode_handler(auth)
        except jwt.ExpiredSignature:
            raise NotAuthenticated('token已过期')
        except:
            raise NotAuthenticated('token非法')

        user = self.authenticate_credentials(payload)
        return (user, auth)

    def authenticate_header(self, request):
        """
        重写该方法会在response header上添加WWW-Authenticate，并且验证失败会使返回的状态变为401，不然是403.
        """
        return 'token'