from MysqldbHelper import *
from django.http import HttpResponse

def updatewhitelist(request):
    whiteMember = request.GET['whiteMember']
    db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
    update = "UPDATE white_list_member set screen_keys = '%s' where user_id = '%s'" % (whiteMember)
    db.update(update)
    return HttpResponse({'succes'})


def selectwhitelist(request):
        UID = request.GET['whitelistuid']
        db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
        sql = "select * from white_list_member where user_id = '%s'" % (UID)
        fc = db.query(sql)
        list = []
        for row in fc:
            member = row[4]
            list.append("whitelist=%s" % \
                        (member))
        if len(list):
            return HttpResponse(list)
        else:
            return HttpResponse('result is null')