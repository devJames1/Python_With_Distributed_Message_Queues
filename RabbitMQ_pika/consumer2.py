import pika

QUEUE_NAME_2 = "mailbox2"

def callback(channel, method, properties, body):
    message = body.decode("utf-8")
    print(f"--cunsumer2-- Got message: {message}")

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.basic_consume(
        queue=QUEUE_NAME_2,
        auto_ack=True,
        on_message_callback=callback
    )
    channel.start_consuming()