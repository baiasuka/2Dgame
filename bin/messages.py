from bin.tools import get_host_ip
from bin.TCPpackage import TCPpackage

class Message:
    host = get_host_ip()

    @classmethod
    def request_roomlist(self):
        data = {'cilent_ip':self.host}
        data['type'] = 'request_roomlist'
        p = TCPpackage()
        p.set_content(data)
        return p.get_pck_with_head()

    @classmethod
    def get_roomlist(self, data):
        roomlist = data['roomlist']
        return roomlist

if __name__ == '__main__':
    pass
