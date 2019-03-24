import os
import glob
class Picfile:
    def __init__(self):
        self.init_pic_obj()

    def init_pic_obj(self):
        """
        动态添加类的属性，每一个属性指向一个图片文件
        :return:
        """
        dir_path = os.path.join(os.path.dirname(__file__))
        print(dir_path)
        file_list = glob.glob1(dir_path, '*.jpg')
        file_list += glob.glob1(dir_path, '*.png')

        pic_attr = [elem[:-4].upper() + '_IMAGE' for elem in file_list]
        pic_path = [os.path.join(os.path.dirname(__file__)) + r'/' + elem for elem in file_list]
        print(pic_attr)
        print(pic_path)
        zipped = zip(pic_attr, pic_path)
        for x, y in zipped:
            setattr(self, x, y)

Pic = Picfile()
