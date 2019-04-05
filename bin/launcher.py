import tkinter
import socket

from bin.tools import get_host_ip, encrypt_md5, PostgresqlConnection

USERNAME = None


# 登录界面
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
        cur = conn.cursor()

        try:
            sql = 'select password from test.users where username = %s'
            cur.execute(sql, [username])
            result = cur.fetchone()
        except:
            print('登录出错')
        else:
            if result is None:
                info = tkinter.Message(self.face, text='该用户不存在')
                info.pack()
            else:
                if result[0] == password:
                    global USERNAME
                    USERNAME = username
                    info = tkinter.Message(self.face, text='登陆成功')
                    info.pack()
                    self.face.destroy()
                    HallSurface(self.mainWindow)
                else:
                    info = tkinter.Message(self.face, text='密码错误')
                    info.pack()
        finally:
            conn.close()


# 大厅界面
class HallSurface:
    def __init__(self, mainWindow):
        self.username = USERNAME

        self.mainWindow = mainWindow
        self.face = tkinter.Frame(self.mainWindow,)
        self.face.pack()

        btn_login = tkinter.Button(self.face, text='登录', command=self.get_roomlist)
        btn_login.pack()

    def get_roomlist(self,):
        pass




if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('登录')
    root.geometry('800x640')

    LoginSurface(root)
    root.mainloop()
