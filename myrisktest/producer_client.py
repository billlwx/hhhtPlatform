#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/17
import sys
from my_producer import *
from django.http import HttpResponse

reload(sys)
sys.setdefaultencoding('utf8')

def sendriskmq(request):
    producer = MyProducer()
    producer.producerriskmq()
    return HttpResponse('success')