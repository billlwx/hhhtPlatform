from MysqldbHelper import *
from django.http import HttpResponse
from django.conf import settings
from django.core.cache import cache
from django_redis import get_redis_connection
import redis


def delete_auth(request):
    pool = redis.ConnectionPool(host='172.18.225.181',port=6379)
    r = redis.StrictRedis(connection_pool=pool)
    id = request.GET['userId']
    key = 'auth_status::'+id
    print key
    r.delete(key)
    return HttpResponse("success")

