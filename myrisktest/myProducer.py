#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/10
import pika
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class myProducer:

    def sendMQ(self):
        exchange = 'ex-case-push'
        # queue='anti_fraud_request_queue'
        # exchange='py_exchange'
        # queue='py_queue'
        connection = pika.BlockingConnection(pika.ConnectionParameters(
        '172.18.225.179'))
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)
        # 声明queue
        # channel.queue_declare(queue=queue)
        # channel.queue_bind(exchange=exchange,queue=queue)
        # n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
        with open('1.txt', 'r') as f:
            for line in f:
               data = line
               channel.basic_publish(exchange=exchange,
                                  routing_key='',
                                  body=data)
            print(" [x] Sent ")
        connection.close()

if __name__ == '__main__':
    Producer = myProducer()
    Producer.sendMQ()