import redis
import threading
from redis import ConnectionPool

pool = ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

pool = ConnectionPool(host='localhost', port=6379, db=0)

r1 = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)

pool = ConnectionPool(host='localhost', port=6379, db=0)

def worker():
    r = redis.Redis(connection_pool=pool)
    # Perform Redis operations with 'r'

threads = [threading.Thread(target=worker) for _ in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

pool = ConnectionPool(
    host='localhost',
    port=6379,
    db=0,
    max_connections=10,
    timeout=5,
    socket_connect_timeout=3,
    socket_keepalive=True
)
r = redis.Redis(connection_pool=pool)
