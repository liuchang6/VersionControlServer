# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 18:58
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : websocket.py
# @Software: PyCharm

import base64
import asyncio
import threading

import tornado.websocket
import paramiko


class MyThread(threading.Thread):
    def __init__(self, id, web_ssh_server):
        threading.Thread.__init__(self)
        self.web_ssh_server = web_ssh_server

    def run(self):
        #解决tornado6版本 提示 There is no current event loop in thread-3 的错误。
        asyncio.set_event_loop(asyncio.new_event_loop())
        while 1:
            try:
                data = self.web_ssh_server.chan.recv(1024)
                if len(data) == 0:
                    break
                self.web_ssh_server.write_message(data)
            except Exception as ex:
                print(str(ex))
                self.web_ssh_server.sshclient.close()
        self.web_ssh_server.sshclient.close()
        return False


class WebSSHServer(tornado.websocket.WebSocketHandler):

    def open(self):

        USERNAME = self.get_argument('user','')
        HOSTS = self.get_argument('host','')
        PORT = self.get_argument('port','')
        PASSWORD = self.get_argument('password','')

        PASSWORD = base64.b64decode(PASSWORD).decode("utf-8")

        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(HOSTS, PORT, USERNAME, PASSWORD)
        self.chan = self.sshclient.invoke_shell(term='xterm',width=130,height=60)

        t1 = MyThread(999, self)
        t1.setDaemon(True)
        t1.start()

    def on_message(self, message):
        try:
            self.chan.send(message)
        except Exception as ex:
            print(str(ex))

    def on_close(self):
        self.sshclient.close()

    def check_origin(self, origin):
        # 允许跨域访问
        return True


if __name__ == '__main__':
    # 定义路由
    app = tornado.web.Application([
        (r"/terminals/", WebSSHServer),
    ],
    )

    # 启动服务器
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(3000)
    tornado.ioloop.IOLoop.current().start()
