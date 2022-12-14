
import pika
from kafka import KafkaProducer

QUEUE_NAME = "mailbox"

# RabbitMQ: pika
with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)
    while True:
        message = input("Message: ")
        channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=message.encode("utf-8")
        )

# Apache Kafka: kafka-python3
