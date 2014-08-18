import os
import redis
from rq import Worker, Queue, Connection

from hello import workerstuff

listen =['high', 'default', 'low']

redis_url= os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')

conn=redis.from_url(redis_url)



q=Queue(connection=workerstuff)
result=q.enqueue(workerstuff)


if __name__ == '__main__':
  with Connection(conn):
    worker=Worker(map(Queue, listen))
    worker.work()
