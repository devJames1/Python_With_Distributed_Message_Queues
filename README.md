# Python With Distributed Message Queues

## Installation

To get started, create and activate a new virtual environment, and then install the required dependencies into it:

```shell
$ python3 -m venv venv/ --prompt=queue
$ source venv/bin/activate
(queue) $ python -m pip install -r requirements.txt -c constraints.txt
```


### Message Brokers

#### RabbitMQ

Start a RabbitMQ broker with Docker:

```shell
$ docker run -it --rm --name rabbitmq -p 5672:5672 rabbitmq
```

Open separate terminal windows, activate your virtual environment, change directory to `message_brokers/rabbitmq/`, and run your producer and consumer scripts:  

```shell
(queue) $ cd message_brokers/rabbitmq/
(queue) $ python producer.py
(queue) $ python consumer.py
```

You can have as many producers and consumers as you like.

#### Redis

Start a Redis server with Docker:

```shell
$ docker run -it --rm --name redis -p 6379:6379 redis
```

Open separate terminal windows, activate your virtual environment, change directory to `message_brokers/redis/`, and run your publisher and subscriber scripts:  

```shell
(queue) $ cd message_brokers/redis/
(queue) $ python publisher.py
(queue) $ python subscriber.py
```

You can have as many publishers and subscribers as you like.

#### Apache Kafka

Change directory to `message_brokers/kafka/` and start an Apache Kafka cluster with Docker Compose:

```shell
$ cd message_brokers/kafka/
$ docker-compose up
```

Open separate terminal windows, activate your virtual environment, change directory to `message_brokers/kafka/`, and run your producer and consumer scripts:  

```shell
(queue) $ cd message_brokers/kafka/
(queue) $ python producer.py
(queue) $ python consumer.py
```

You can have as many producers and consumers as you like.