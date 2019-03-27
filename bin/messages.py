from bin.tools import get_host_ip
from bin.TCPpackage import TCPpackage

HOST = get_host_ip()

class Message:
    host = HOST

    @classmethod
    def request_roomlist(cls):
        data = {'cilent_ip':cls.host}
        data['type'] = 'request_roomlist'
        p = TCPpackage()
        p.set_content(data)
        return p.get_pck_with_head()

    def parse_roomlist(self,msg):

if __name__ == '__main__':
    print(Message.request_roomlist())
