# You connect to a local Redis server instance and immediately
#  start publishing messages on the chatroom channel. 
# You don’t have to create the channels, because Redis
#  will do it for you. Subscribing to a channel requires 
# one extra step, creating the PubSub object to call the .subscribe() 
# method on:

import redis

with redis.Redis() as client:
    pubsub = client.pubsub()
    pubsub.subscribe("chatroom1")
    for message in pubsub.listen():
        if message["type"] == "message":
            body = message["data"].decode("utf-8")
            print(f"Got message: {body}")