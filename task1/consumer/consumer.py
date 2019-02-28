#!/usr/bin/env python
import pika
import random
import time

def connect_to_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
            channel = connection.channel()
            channel.queue_declare(queue='hello')    
            return (connection, channel)
        except (pika.exceptions.ConnectionClosed, OSError):
            time.sleep(2)
            print("I need to retry")

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

connection, channel = connect_to_rabbitmq()
channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
