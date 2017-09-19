from MysqldbHelper import *
from django.http import HttpResponse

def selectUid(request):
    mobile = request.GET['mobile']
    db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
    sql = "select * from user where mobile like '%%%%%s%%%%'" % (mobile)
    fc = db.query(sql)
    list = []
    for row in fc:
        id = row[0]
        mobile = row[1]
        list.append("id=%s,mobile=%s" % \
              (id, mobile))
    return HttpResponse(list)