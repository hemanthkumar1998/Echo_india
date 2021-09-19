import redis
import time
from redisHelper import redis_pool


reciever =  redis.Redis(connection_pool=redis_pool,port=6379)
try:
    print("Reciever is listening ....")

    while reciever.exists("random_number"):
        value = reciever.get("random_number")
        print(value)
        time.sleep(2)
except Exception as ex:
    print(f"Reciever has stopped {ex}")