import socket
from hashlib import md5
import psycopg2
from sqlalchemy import create_engine
from bin.settings import config

def get_host_ip():
    """
    获取用户电脑的ip地址
    :return:
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def encrypt_md5(data, times=1):
    """
    对密码进行加密操作，数据库中不会保存真实密码
    :param data: 要加密的数据
    :param times: 解密的次数
    :return:
    """
    m5 = md5()
    for i in range(times):
        m5.update(data.encode("utf-8"))
        data = m5.hexdigest()
    return data

class PostgresqlConnection(object):
    def __init__(self, host=None, port=None, username=None, password=None, db_name=None):
        self.host = host if host else config.DB_HOST
        self.port = port if port else config.DB_PORT
        self.username = username if username else config.DB_USER
        self.password = password if password else config.DB_PASSWORD
        self.dbs = db_name if db_name else config.DB_NAME

        self.conn = self.connect_2_db()
        self.cursor = self.conn.cursor()

    def connect_2_db(self):
        import os
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        conn = psycopg2.connect(database=self.dbs, user=self.username, password=self.password, host=self.host, port=self.port)
        return conn

    def insert_sql(self, sql=None):
        if not sql:
            return None
        try:
            self.cursor.execute(sql)
            self.commit()
            self.disconnect_2_db()
            return True
        except Exception as e:
            print(e.message)
            return False

    def update_sql(self, sql=None, params=None):
        if not sql:
            return None
        try:
            self.cursor.execute(sql, params)
            self.commit()
            self.disconnect_2_db()
            return True
        except Exception as e:
            print(e.message)
            return False

    def disconnect_2_db(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        return self.cursor

    def commit(self):
        return self.conn.commit()

    def get_engine(self):
        print(self.dbs)
        return create_engine('postgresql://{username}:{password}@{host}:{port}/{dbs}'.format(
            username=self.username, password=self.password, host=self.host, port=self.port, dbs=self.dbs))