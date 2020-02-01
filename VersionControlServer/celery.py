# -*- coding: utf-8 -*-
# @Time    : 2019/2/01 8:29
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : celery.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VersionControlServer.settings')

app = Celery('VersionControlServer')#项目名称

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

