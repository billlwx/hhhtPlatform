from MysqldbHelper import *
from django.http import HttpResponse
from django.conf import settings
from django.core.cache import cache
from django_redis import get_redis_connection
import redis


def delete_auth(request):
    r = redis.ConnectionPool(host='172.18.225.181',port=6379)
    id = request.GET['userId']
    key = 'auth_status::'+id
    print key
    r.delete(key)
    return HttpResponse("success")

