import redis
r = redis.StrictRedis(host='10.1.1.253', port=6379, db=0)
for key in r.scan_iter("key_pattern*"):
    print (key)
