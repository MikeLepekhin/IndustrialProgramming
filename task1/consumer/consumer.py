#!/usr/bin/env python
import pika
import random
import time
import psycopg2

print("[x] consumer started")

while True:
    try:
        db_connect = psycopg2.connect(
            host="postgres", 
            database="postgres", 
            user="postgres",
            password="postgres"
        )
    except psycopg2.Error:
        print('consumer need to rconnect to database')
        time.sleep(3)
    else:
        break


db_cursor = db_connect.cursor()
db_cursor.execute("CREATE TABLE IF NOT EXISTS randnums (id SERIAL PRIMARY KEY, num INT)")
db_cursor.close()
db_connect.commit()
add_number_query = "INSERT INTO randnums (num) VALUES (%s)"
print("[x] connection to database established")

def callback(ch, method, properties, body):
    print("[x] reveived " + str(body))
    cursor = db_connect.cursor()
    #body_value = int.from_bytes(body, byteorder="little")
    body_value = int(body)    
    cursor.execute(add_number_query, [body_value])
    cursor.close()
    db_connect.commit()

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue='hello')   
        channel.basic_consume(callback, queue='hello')
        channel.start_consuming()
    except (pika.exceptions.ConnectionClosed, OSError):
        time.sleep(1)
        print("I need to retry")
        

