from bin.tools import get_host_ip
from bin.TCPpackage import TCPpackage

class Message:
    host = get_host_ip()

    @classmethod
    def package_roomlist(cls):
        data = {'cilent_ip':cls.host}
        data['type'] = 'request_roomlist'
        p = TCPpackage()
        p.set_content(data)
        return p.get_pck_with_head()

    @classmethod
    def parse_roomlist(self,msg):
        p = TCPpackage(msg)
        data = p.get_content()
        roomlist = data['roomlist']
        return roomlist

if __name__ == '__main__':
    pass
