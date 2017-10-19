#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/17
import sys
from my_producer import *
from django.http import HttpResponse
from apo.zidian import *
from apo.MysqldbHelper import *

reload(sys)
sys.setdefaultencoding('utf8')

def sendriskmq(request):
    producer = MyProducer()
    producer.producerriskmq()
    return HttpResponse('success')

def sendlendrulesmq(request):
    handleResult = request.GET.get('handleResult')
    mobile = request.GET.get('mobile')
    if mobile == "":
       return HttpResponse("手机号不能为空")
    else:
        sql = "SELECT case_no FROM `case` WHERE mobile=%s ORDER BY id desc limit 1;" % (mobile)
        db = DB(**cgg_test_db)
        fc = db.query(sql)
    if fc == ():
        return HttpResponse('请输入正确的手机号')
    for row in fc:
        taskID = row[0]
    MQ = '''{"engineDetails":"测试组模拟数据","handleResult":"%s","object":[{"timestamp":"100","type":"3"},{"timestamp":"100","type":"2"},{"timestamp":"100","type":"1"},{"timestamp":"100","type":"4"},{"timestamp":"100","type":"5"},{"timestamp":"100","type":"6"},{"timestamp":"100","type":"7"},{"timestamp":"100","type":"8"},{"timestamp":"100","type":"9"},{"timestamp":"100","type":"10"},{"timestamp":"100","type":"11"}],"phoneNum":"%s","score_info":[{"creditAmount":-1,"score":500,"scorecard_type":"1","startTime":1508226996660,"validDays":90}],"taskID":"%s"}''' % (handleResult, mobile, taskID)
    producer = MyProducer()
    producer.producerlendrulesmq(MQ)
    return HttpResponse('推送成功')