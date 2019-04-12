import pickle
import copy

# 通过在数据前增加数据长度段来分割粘连包
# 数据长度段的长度为4字节
# 数据域统一为字典经过utf-8编码后的字符串

class TCPpackage:
    def __init__(self, pck=None):
        if pck:
            self._content = bytearray(pck)
        else:
            self._content = bytearray(0)

    def get_content(self):
        """
        将数据域数据转化为字典返回
        :return:
        """
        try:
            content = self._content
            content = content.decode(encoding='utf-8')
            return eval(content)
        except:
            raise Exception("解析数据异常！")

    def set_content(self, data):
        data = str(data)
        self._content = bytearray(data.encode(encoding='utf-8'))

    def get_pck_with_head(self):
        pck_length = bytearray(len(self._content).to_bytes(4, byteorder='little'))
        return pck_length + self._content


if __name__ == '__main__':
    pass
