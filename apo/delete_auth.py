from MysqldbHelper import *
from django.http import HttpResponse
from django.conf import settings
from django.core.cache import cache
from django_redis import get_redis_connection


def delete_auth(request):
    id = request.GET['userId']
    key = 'auth_status::'+id
    print key
    cache.delete_pattern("auth_status::136249")
    return HttpResponse("success")

