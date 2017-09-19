# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from MysqldbHelper import *

# Create your views here.

def index(request):

    return render_to_response('index.html')



def search(request):
    mobile = request.get['mobile']
    db = DB('119.23.218.196', 33066, 'admin', 'admin#ROOT@ha', 'miloan')
    sql = "select * from user where mobile like %'%d'%" % (mobile)
    fc = db.query(sql)
    list = []
    for row in fc:
        id = row[0]
        mobile = row[1]
        list.append("id=%s,mobile=%s" % \
              (id, mobile))
    return HttpResponse(list)

