# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 10:22
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : jwt_handler.py
# @Software: PyCharm

def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和success信息
    """
    return {
        'token': token,
        'success': True
    }

def jwt_response_payload_error_handler(serializer):
    """
    设置jwt登录失败之后返回message信息
    """
    return {
        "msg": "用户名或者密码错误",
        "detail": serializer.errors
    }