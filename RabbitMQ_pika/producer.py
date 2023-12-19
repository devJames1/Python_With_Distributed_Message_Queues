# RabbitMQ is probably one of the most popular open sourcemessage brokers, which lets you route messages from producers to consumers
#  in several ways. You can conveniently start a new RabbitMQ broker without installing it on your computer by running a temporary
# Docker container:

import pika 

QUEUE_NAME_1 = "mailbox"
QUEUE_NAME_2 = "mailbox2"

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channe2 = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME_1)
    channe2.queue_declare(queue=QUEUE_NAME_2)
    while True:
        message = input("Mesaage: ")
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME_1,
            body=message.encode("utf-8")
        )

        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME_2,
            body=message.encode("utf-8")
        )