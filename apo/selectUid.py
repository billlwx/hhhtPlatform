from MysqldbHelper import *
from django.http import HttpResponse
from zidian import *

def selectUid(request):
    mobile = request.GET['mobile']
    db = DB(**cgg_test_db)
    sql = "select * from user where mobile like '%%%%%s%%%%'" % (mobile)
    fc = db.query(sql)
    list = []
    for row in fc:
        id = row[0]
        mobile = row[1]
        list.append("id=%s,mobile=%s" % \
              (id, mobile))
    if len(list):
        return HttpResponse(list)
    else:
        return HttpResponse('result is null')
