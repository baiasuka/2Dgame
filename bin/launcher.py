import tkinter
import socket

from bin.tools import get_host_ip, encrypt_md5, PostgresqlConnection

class LoginSurface:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.face = tkinter.Frame(self.mainWindow,)
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
                sql = 'select password from test.test where username = %s'
                result = cur.execute(sql, (username))
        except:
            raise print('登录出错')
        else:
            if result == 0:
                info = tkinter.Message(self.face, text='该用户不存在')
                info.pack()
            else:
                if cur.fetchone()[0] == password:
                    info = tkinter.Message(self.face, text='登陆成功')
                    info.pack()
                    self.face.destroy()
                    HallSurface(self.mainWindow)
                else:
                    info = tkinter.Message(self.face, text='密码错误')
                    info.pack()


class HallSurface:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.face = tkinter.Frame(self.mainWindow,)
        self.face.pack()

        pass




if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('登录')
    root.geometry('200x200')

    LoginSurface(root)
    root.mainloop()
