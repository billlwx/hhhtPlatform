# -*- encoding:utf8 -*-
'''
@author: crazyant.net
@version: 2013-10-22

封装的mysql常用函数
'''
from django.http import HttpResponse



import MySQLdb


class DB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

        self.conn = self.getConnection()

    def getConnection(self):
        return MySQLdb.Connect(
            host=self.DB_HOST,  # 设置MYSQL地址
            port=self.DB_PORT,  # 设置端口号
            user=self.DB_USER,  # 设置用户名
            passwd=self.DB_PWD,  # 设置密码
            db=self.DB_NAME,  # 数据库名
            charset='utf8'  # 设置编码
        )

    def query(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        returnData = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return returnData

    def update(self, sqlString):
        try:
            cursor = self.conn.cursor()
            # 执行sql语句
            cursor.execute(sqlString)
            # 提交到数据库执行
            self.conn.commit()
            cursor.close()
        except:
            # Rollback in case there is any error
            self.conn.rollback()
        # 关闭数据库连接
        self.conn.close()

    def insert(self, sqlString):
        try:
                cursor = self.conn.cursor()
                # 执行sql语句
                cursor.execute(sqlString)
                # 提交到数据库执行
                self.conn.commit()
        except:
            self.conn.rollback()
        # 关闭数据库连接
        self.conn.close()


