from MysqldbHelper import *
from django.http import HttpResponse

def updatewhitelist(request):
    UID = request.GET['userId']
    db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
    updatecase = "UPDATE white_list_member set screen_keys = '%s' where user_id like '%%%%%s%%%%'" % (UID)
    updatecontr = "UPDATE miloan.contract set status = 'REPAY_SUC'  where uid = '%s' ORDER BY id desc  limit 1" % (UID)
    db.update(updatecase)
    db.update(updatecontr)
    return HttpResponse({'succes'})


def selectwhitelist(request):
        UID = request.GET['uid']
        db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
        sql = "select * from white_list_member where user_id like '%%%%%s%%%%'" % (UID)
        fc = db.query(sql)
        list = []
        for row in fc:
            member = row[4]
            list.append("白名单为%s" % \
                        (member))
        if len(list):
            return HttpResponse(list)
        else:
            return HttpResponse('result is null')