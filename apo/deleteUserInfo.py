from MysqldbHelper import *
from django.http import HttpResponse
import redis
from zidian import *

def deleteUserInfo(request):
    mobile = request.GET['uid']

    list = ['user_contact', 'user_contact_archive', 'user_employment', 'user_employment_archive',
            'user_employment_status', 'user_identity', 'user_identity_archive', 'user_identity_face',
            'user_identity_face_archive', 'user_identity_face_status', 'user_key_contact', 'user_operator',
            'user_operator_archive', 'user_operator_status', 'user_personal_status', 'user_receipt',
            'user_receipt_archive', 'user_receipt_status', 'user_wechat', 'user_wechat_archive', 'user_wechat_status',
            'user_zhima', 'user_zhima_archive', 'user_zhima_status']
#    sql = "select * from user where mobile like '%%%%%s%%%%'" % (mobile)
#    fc = db.query(sql)
    for i in list:
        table_name = i
        sql = "DELETE from %s where user_id = '%s'" % (table_name,mobile)
        deletedb = DB(**cgg_test_db)
        deletedb.update(sql)
    return HttpResponse({'succes'})


def modifyUserInfo(request):
    UID = request.GET['modifyUserUid']
    updatecase = "UPDATE miloan.case set case_status = 'rejected' where user_id = '%s' ORDER BY id desc  limit 1" % (UID)
    db = DB(**cgg_test_db)
    db.update(updatecase)
    updatecontr = "UPDATE miloan.contract set status = 'REPAY_SUC'  where uid = '%s' ORDER BY id desc  limit 1" % (UID)
    contrdb = DB(**cgg_test_db)
    contrdb.update(updatecontr)
    return HttpResponse({'succes'})



def delete_auth(request):
    pool = redis.ConnectionPool(host='172.18.225.181',port=6379)
    r = redis.StrictRedis(connection_pool=pool)
    id = request.GET['userId']
    key = 'auth_status::'+id
    print key
    r.delete(key)
    return HttpResponse("success")

