#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host='119.23.218.196', port=33066, user='admin', passwd='admin#ROOT@ha', db='miloan', charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# 删除数据表SQL语句
sql = "select * from user where mobile like '%d'"%(18310709835)

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
 #  db.commit()
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      mobile = row[1]
      print "id=%s,mobile=%s" % \
         (id, mobile)

except:
   # 发生错误时回滚

   print "Error: unable to fecth data"
 #  db.rollback()

# 关闭数据库连接
db.close()