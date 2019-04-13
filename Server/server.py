import socket
from threading import Thread
from .TCPpackage import TCPpackage

SERVER_PORT = 9998

class ServerCore():
    def __init__(self):
        self.port = SERVER_PORT
        self.socket = self.create_socket()

    def create_socket(self, backlog=5):
        serversocket = socket.socket()
        serversocket.bind(('127.0.0.1',self.port))
        serversocket.listen(backlog)

        return serversocket

    def pck_sender(self):
        """
        用于服务器发消息
        :return:
        """
        pass

    def pck_handler(self):
        while True:
            conn, addr = self.socket.accept()
            msg_recv = conn.recv(1024).decode('utf-8')
            print("收到来自ip：%s 的信息：%s" % (str(addr), str(msg_recv)))
            bytes = conn.recv(1024)
            while len(bytes) > 0:
                # 获取包长度
                pck_length = int.from_bytes(bytes[:4], byteorder='little')
                # 截取包里的内容
                pck_content = bytes[4:4 + pck_length]
                # 删除已截取的内容
                bytes = bytes[4 + pck_length]
                # 解析内容
                data = TCPpackage(pck_content).get_content()
