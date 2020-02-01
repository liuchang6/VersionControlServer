# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 16:24
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
import datetime

from celery import shared_task

from version_control.utils.git_tool import GitRepository
from version_control.utils.ssh_tool import CheckSSH
from version_control.models import ServerInfo,RepositoryInfo

def get_all_server_info():
	return ServerInfo.objects.all()

def get_all_repository_info():
	return RepositoryInfo.objects.all()

@shared_task()
def check_server_status():
	for server_obj in get_all_server_info():
		ssh = CheckSSH(server_obj.ip, server_obj.port, server_obj.user, server_obj.password)
		if ssh.sshConnect():
			ServerInfo.objects.filter(id=server_obj.id).update(status=1, check_time=datetime.datetime.now())
		else:
			ServerInfo.objects.filter(id=server_obj.id).update(status=0, check_time=datetime.datetime.now())

@shared_task()
def check_git_status():
	for repository_obj in get_all_repository_info():
		repository = GitRepository(repository_obj.user, repository_obj.password, repository_obj.url, local_path=repository_obj.password)
		branches = repository.get_branch()
		if type(branches) == list:
			RepositoryInfo.objects.filter(id=repository_obj.id).update(status=1, check_time=datetime.datetime.now(),branches = branches)
		else:
			RepositoryInfo.objects.filter(id=repository_obj.id).update(status=0, check_time=datetime.datetime.now(),branches = '')


