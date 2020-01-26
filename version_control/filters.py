# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 14:58
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : filters.py
# @Software: PyCharm

import django_filters
from version_control.models import ServerInfo
class ServerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='contains')
    ip = django_filters.CharFilter(field_name="ip", lookup_expr='contains')

    class Meta:
        model = ServerInfo
        fields = ['name','ip']