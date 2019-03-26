import tkinter
import socket

from bin.tools import get_host_ip, encrypt_md5, PostgresqlConnection

class LoginSurface:
    def __init__(self, mainface):
        self.mainface = mainface
        self.face = tkinter.Frame(self.mainface,)
        self.face.pack()

        tkinter.Label(self.face, text='用户名').pack()
        self.e_username = tkinter.Entry(self.face,)
        self.e_username.pack()

        tkinter.Label(self.face, text='密码').pack()
        self.e_password = tkinter.Entry(self.face,)
        self.e_password.pack()

        btn_login = tkinter.Button(self.face, text='登录', command=self.login)
        btn_login.pack()

        def login(self,):
            username = self.e_username.get()
            password = self.e_password.get()
            password = encrypt_md5(password)

            conn = PostgresqlConnection().conn
            try:
                with conn.cursor() as cur:
                    pass
            except:
                raise print('登录出错')
            else:
                if result == 0:
                    tkinter.tkMessageBOX()




if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('登录')
    root.geometry('200x200')
