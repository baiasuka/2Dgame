import pickle
import copy

# 通过在数据前增加数据长度段来分割粘连包
# 数据长度段的长度为4字节

class TCPpackage:
    def __init__(self, pck=None):
        if pck:
            self._content = bytearray(pck)
        else:
            self._content = bytearray(0)

    def get_content(self):
        try:
            content = self._content[4:]
            return content.decode(encoding='utf-8')
        except:
            raise Exception("解析数据异常！")

    def set_content(self,data):
        data = str(data)
        self._content = bytearray(data.encode(encoding='utf-8'))

    def get_pck_with_head(self):
        pck_length = bytearray(len(self._content).to_bytes(4, byteorder='little'))
        return pck_length + self._content

