from django.conf import settings
from django.core.cache import cache


#delete auth  uid
def delete_auth(self, uid):
    key = 'auth_status::'+uid
    cache.delete(key)


#write cache user id
def write_to_cache(self, user_name):
    key = 'user_id_of_'+user_name
    cache.set(key, json.dumps(user_name), settings.NEVER_REDIS_TIMEOUT)