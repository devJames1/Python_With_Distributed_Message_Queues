# Kafka is by far the most advanced and complicated of the
#  three message brokers you’ll meet in this tutorial. It’s
#  a distributed streaming platform used in real-time
#  event-driven applications. Its main selling point is
#  the ability to handle large volumes of data with almost
#  no performance lag.

# To run Kafka, you’ll need to set up a distributed cluster. You may use Docker Compose to start a multi-container Docker application in

# When you save this configuration in a file named docker-compose.yml,
#  then you can start the two services by running the command below:
# $ docker-compose up

from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    message = input("Message: ")
    producer.send(
        topic="datascience",
        value=message.encode("utf-8"),
    )

# The .send() method is asynchronous because it returns a future object that you
    #  can await by calling its blocking .get() method. On the consumer’s side,
    #  you’ll be able to read the sent messages by iterating over the consumer: