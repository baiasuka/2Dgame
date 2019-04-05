# -*- coding: UTF-8 -*-

import socket
import sys

from bin.tools import get_host_ip
from bin.TCPpackage import TCPpackage
from bin.messages import Message

SERVER_IP = '139.196.254.177'
SERVER_PORT = 9998
CILENT_PORT = 9997

class CilentCore:
    def __init__(self):
        self.host = get_host_ip()
        self.port = CILENT_PORT

    def create_socket(self):
        cilentsocket = socket.socket()
        cilentsocket.connect((SERVER_IP, SERVER_PORT))
        return cilentsocket

    def msg_sender(self):
        """
        用于发送消息给服务器
        :return:
        """
        pass

    def msg_handler(self):
        cilentsocket = self.create_socket()
        while True:
            bytes = cilentsocket.recv(1024)
            while len(bytes) > 0:
                pass


while __name__ == '__main__':
    pass
    # cilentsocket = CilentCore.create_socket()
    #
    #
    # msg = input('请输入要发送的信息：').strip()
    # cilentsocket.send(msg.encode('utf-8'))
    #
    # print(cilentsocket.recv(1024).decode('utf-8'))
    # cilentsocket.close()