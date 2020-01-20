# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 18:58
# @Author  : changliu
# @Email   : 499926587@qq.com
# @File    : websocket.py
# @Software: PyCharm
import base64
import threading

import tornado.websocket
import paramiko


class MyThread(threading.Thread):
    def __init__(self, id, chan):
        threading.Thread.__init__(self)
        self.chan = chan

    def run(self):
        while not self.chan.chan.exit_status_ready():
            try:
                data = self.chan.chan.recv(1024)
                print(data)
                if len(data) == 0:
                    break
                self.chan.write_message(data)

            except Exception as ex:
                print(str(ex))
        self.chan.sshclient.close()
        return False



class WebSSHServer(tornado.websocket.WebSocketHandler):

    def open(self):
        USERNAME = self.get_argument('user','')
        HOSTS = self.get_argument('host','')
        PORT = int(self.get_argument('port',''))
        PASSWORD = self.get_argument('password','')
        if PASSWORD:
            PASSWORD = base64.b64decode(PASSWORD).decode('utf-8')
        else:
            PASSWORD = None
        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(HOSTS, PORT, USERNAME, PASSWORD)
        self.chan = self.sshclient.invoke_shell(term='xterm',width=800,height=600)
        t1 = MyThread(1, self)
        t1.setDaemon(True)
        t1.start()

    def on_message(self, message):
        try:
            print(message)
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
