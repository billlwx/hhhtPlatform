from MysqldbHelper import *
from django.http import HttpResponse
from django.conf import settings
from django.core.cache import cache


def delete_auth(request):
    id = request.GET['userId']
    key = 'auth_status::'+id
    print key
    cache.delete(key)
    return HttpResponse({'succes'})