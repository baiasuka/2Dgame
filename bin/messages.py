from bin.tools import get_host_ip
from bin.TCPpackage import TCPpackage

class MessageHandler:
    def __init__(self, data):
        self.data = data
        self.host = get_host_ip()

    def handle(self):
        if self.data['type'] == 'roomlist':
            pass


    @classmethod
    def get_roomlist(self, data):
        roomlist = data['roomlist']
        return roomlist

class MessageSender:
    host = get_host_ip()

if __name__ == '__main__':
    pass
