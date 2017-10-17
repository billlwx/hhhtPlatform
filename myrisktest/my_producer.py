#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/17
import pika
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MyProducer:

    def producerriskmq(self):
        exchange = 'ex-case-push'
        # queue='anti_fraud_request_queue'
        # exchange='py_exchange'
        # queue='py_queue'
        try:
           connection = pika.BlockingConnection(pika.ConnectionParameters(
            '172.18.225.179'))
           channel = connection.channel()
           channel.exchange_declare(exchange=exchange, exchange_type='fanout', durable=True)
        except (BaseException), e:
            print e
        # 声明queue
        # channel.queue_declare(queue=queue)
        # channel.queue_bind(exchange=exchange,queue=queue)
        # n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
        try:
            with open('/home/apps/bill/rabbitmq.txt', 'r') as f:
                for line in f:
                  data = line
                channel.basic_publish(exchange=exchange,
                                  routing_key='',
                                  body=data)
                print(" [x] Sent ")
            connection.close()
        except (BaseException), e:
            print e

