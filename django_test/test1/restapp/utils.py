from redis.client import StrictRedis

redis = StrictRedis(host='localhost',port=6379,db=0,password='')