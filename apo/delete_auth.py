from MysqldbHelper import *
from django.http import HttpResponse
from django.conf import settings
from django.core.cache import cache


def delete_auth(request):
    userId = request.GET['uid']
    key = 'auth_status::'+userId
    cache.delete(key)
