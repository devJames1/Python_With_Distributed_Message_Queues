import pika

QUEUE_NAME_1 = "mailbox"

def callback(channel, method, properties, body):
    message = body.decode("utf-8")
    print(f"--cunsumer1-- Got message: {message}")

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.basic_consume(
        queue=QUEUE_NAME_1,
        auto_ack=True,
        on_message_callback=callback
    )
    channel.start_consuming()