# Redis is short for Remote Dictionary Server, but it’s really 
# many things in disguise. It’s an in-memory key-value data store that usually
#  works as an ultra-fast cache between a traditional SQL database 
# and a server. At the same time, it can serve as a persistent NoSQL
#  database and also a message broker in the publish-subscribe model. 
# You can start a local Redis server with Docker:

import redis

with redis.Redis() as client:
    while True:
        message = input("Message: ")
        client.publish("chatroom1", message)
        # client.publish("chatroom2", message)