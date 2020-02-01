# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 14:56
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : git_tool.py
# @Software: PyCharm
import subprocess
import os
os.environ['GIT_PYTHON_REFRESH'] = 'quiet'

from git.repo.fun import is_git_dir
from git.repo import Repo
# 创建版本库对象

TIMEOUT = 1

class GitRepository(object):
    """
    git仓库管理
    """

    def __init__(self, user,passwd, repo_url,type='http',local_path='/tmp'):
        try:
            if type == 'http' or type == 'https':
                repo_url = type+'://'+user+':'+passwd+'@'+repo_url.split('//')[1]
                print(repo_url)
        except :
            pass
        self.local_path = local_path
        self.repo_url = repo_url
        self.repo = None


    def initial(self,branch='master'):
        """
        初始化git仓库
        :param repo_url:
        :param branch:
        :return:
        """
        if not os.path.exists(self.local_path):
            os.makedirs(self.local_path)

        git_local_path = os.path.join(self.local_path, '.git')
        if not is_git_dir(git_local_path):
            self.repo = Repo.clone_from(self.repo_url, to_path=self.local_path, branch=branch)
        else:
            self.repo = Repo(self.local_path)

    def pull(self):
        """
        从线上拉最新代码
        :return:
        """
        self.repo.git.pull()

    def commits_log(self):
        """
        获取所有提交记录
        :return:
        """
        commit_log = self.repo.git.log('--pretty={"commit":"%h","author":"%an","summary":"%s","date":"%cd"}',
                                       max_count=50,
                                       date='format:%Y-%m-%d %H:%M')
        log_list = commit_log.split("\n")
        return [eval(item) for item in log_list]

    def git_cmd(self,cmd):
        return subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate(timeout=10)

    def get_branch(self):
        branches = []
        check_cmd = 'git ls-remote -h %s'%self.repo_url
        try:
            info = self.git_cmd(check_cmd)
            if 'Authentication failed' in str(info) or 'Could not read from remote repository' in  str(info):
                return 'AuthenticationFailed'
        except:
            return 'TimeOut'
        if 'heads' in str(info):
            for i in str(list(info)[0],encoding = "utf-8").split('\n'):
                if i.split().__len__()>1:
                    branch = i.split()[1].split('/')[-1]
                    lable = {}
                    lable["value"] = branch
                    lable["label"] = branch

                    if branch is not None:
                        branches.append(lable)
        return branches

if __name__ == '__main__':
    '''
    python 虚拟环境使用gitpython注意：
    可能虚拟环境的环境变量和本地机器的环境变量不一样，需要添加git到环境变量
    1.添加环境变量 os.putenv('GIT_PYTHON_REFRESH','quiet')
    2.添加环境变量 os.putenv('path','C:\Program Files\Git\cmd')
    '''
    os.putenv('path','C:\Program Files\Git\cmd')
    local_path = 'E:\\git_test16'
    git_repo = 'http://git.baifendian.com/zhengqiGroup/DataService.git'
    repo = GitRepository('chang.liu','!Liu7792049',git_repo,local_path='/tmp')
    repo.initial()
    print(repo.get_branch())
    #repo.pull()
    #print(repo.commits_log())