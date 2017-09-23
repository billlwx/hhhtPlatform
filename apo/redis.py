import redis
import time
## Connect local redis service


client =redis.Redis(host='172.18.225.181',port=6379)
print "Connection to server successfully!"
dicKeys = client.keys("*")
print dicKeys


# Delete key w3ckey
client.delete('auth_status*')
