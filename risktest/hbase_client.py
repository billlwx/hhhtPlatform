#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/10
import sys
from hbase_helper import *
from django.http import HttpResponse

reload(sys)
sys.setdefaultencoding('utf8')

table_adict = {'cp_kv': 'time', 'databank': 'f', 'imei_kv': 'time','ip_imei_kv': 'time', 'ip_kv': 'time',
               'lc_100m_kv': 'time', 'lc_1km_imei_kv': 'time','p8_kv': 'time', 'udid_certno_kv': 'f',
               'contact_mobile_kv': 'f', 'np_kv': 'time', 'risk_control_result': 'f', 'imei_phone_kv': 'time'}

def hbaseclean(request):
    client = HbaseClient()
    i = 0
    for k in table_adict:
        client.table_drop(k)
        client.table_create(k, table_adict[k])
        i = i + 1
    if i == 13:
        return HttpResponse('success')
    else:
        return HttpResponse('false')

