# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 17:24
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : ssh_tool.py
# @Software: PyCharm
import paramiko


class SSH:
    '''
    创建 ssh 连接函数
    hostname, port, username, password,访问linux的ip，端口，用户名以及密码
    '''
    def __init__(self,hostname,port,username,password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def sshConnect(self):

        try:
            sshClient = paramiko.SSHClient()
            sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshClient.connect(self.hostname, self.port, self.username, self.password,timeout=10)
            print("SSH链接成功")
        except Exception as e:
            print("SSH链接失败：[hostname:%s];[username:%s];[error:%s]" %(self.hostname,self.username,e))
            return False
        return sshClient
    '''
    创建命令执行函数
    command 传入linux运行指令
    '''
    def sshExecCmd(self,sshClient,command):

        stdin, stdout, stderr = sshClient.exec_command(command)
        filesystem_usage = stdout.readlines()
        return filesystem_usage
    '''
    关闭ssh
    '''
    def sshClose(self,sshClient):
        sshClient.close()




if __name__ == "__main__":
    info = {
        'host':'172.24.8.133',
        'username':'root',
        'pwd':'jHdCGHMn+Xs=',
        'port':'3222'

    }
    _ssh = SSH('172.24.8.133','3222','root','jHdCGHMn+Xs=')
    _ssh.sshConnect()