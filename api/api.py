from MysqldbHelper import *

if __name__ == "__main__":
    db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
    sql = "select * from user where mobile like '%d'" % (18310709835)
    fc = db.query(sql)
    for row in fc:
        id = row[0]
        mobile = row[1]
        print "id=%s,mobile=%s" % \
              (id, mobile)
