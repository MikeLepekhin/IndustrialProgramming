#!/usr/bin/env python
import pika
import random
import time

max_int = 1e6
range_left_bound = random.randint(0, max_int)
range_length = random.randint(0, max_int)
range_right_bound = range_left_bound + range_length

def my_rand():
    return random.randint(range_left_bound, range_right_bound)

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

connection, channel = connect_to_rabbitmq()
while True:
    new_rand = my_rand()
    channel.basic_publish(exchange='', routing_key='hello', body=str(new_rand))
    print("send " + str(new_rand))
    time.sleep(random.randint(1, 6))

connection.close()

    

