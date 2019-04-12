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
        self.cilentsocket = self.create_socket()

    def create_socket(self):
        cilentsocket = socket.socket()
        cilentsocket.connect((SERVER_IP, SERVER_PORT))
        return cilentsocket

    def pck_sender(self, msg):
        """
        用于发送消息给服务器
        :return:
        """
        pass

    def pck_handler(self):
        """
        去掉包长度并获取数据域数据，将数据域数据传给msg_handler进一步处理
        :return:
        """
        cilentsocket = self.cilentsocket
        while True:
            bytes = cilentsocket.recv(1024)
            while len(bytes) > 0:
                # 获取包长度
                pck_length = int.from_bytes(bytes[:4], byteorder='little')
                # 截取包里的内容
                pck_content = bytes[4:4 + pck_length]
                # 删除已截取的内容
                bytes = bytes[4 + pck_length]
                # 解析内容
                self.msg_handler(pck_content)

    @classmethod
    def msg_handler(self,msg):
        """
        将数据域数据转化为字典后，根据消息类型做处理
        :param msg:
        :return:
        """
        data = TCPpackage(msg).get_content()
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