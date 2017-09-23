import redis

pool = redis.ConnectionPool(host='0.0.0.0', port=6379)
r = redis.Redis(connection_pool=pool)
r.delete("auth_status::136249")