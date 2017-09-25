import memcache
from django.http import HttpResponse

def mcflush(request):
    mc = memcache.Client(['172.18.225.181:11211'], debug=True)
    mc.flush_all()
    return HttpResponse("success")