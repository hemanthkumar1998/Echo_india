import redis
from redisHelper import redis_pool
import time ,random, keyboard

try:
    redis_pool = redis.ConnectionPool(host="localhost",port=6379)
    publisher = redis.Redis(connection_pool=redis_pool)
    
    print("Publisher is up and running ....")
    while True:
        random_number = random.randint(1,1000)
        publisher.set("random_number",random_number)
        print(f"published {random_number}")
        time.sleep(2)

except Exception as ex:
    print(f"Publisher has been stopped {ex}")