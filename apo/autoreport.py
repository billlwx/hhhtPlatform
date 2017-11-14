# -*- coding: utf-8 -*-


from django.http import HttpResponse
import os,sys
import json

def autoreportlist(request):
    #服务器上的地址
    path = '/apps/data/act/autoreport'
    #本地地址
    #path = '/Users/zhouyahui/code/hhht/static/report'
    #  path = '/Users/zhouyahui/code/hhht/static/report'
    reporturl = 'http://119.23.218.196:7081/autoreport/'
    reportlist = []
    for file in os.listdir(path):
        obj= {
            'filename': file,
            'url': reporturl + file
        }

        reportlist.append(obj);
        # reportlist.append("filename=%s,url=%s%s;" % \
        #                  (file,reporturl,file))
    if len(reportlist):
        return  HttpResponse(json.dumps(reportlist, ensure_ascii=False))

    else:
        return HttpResponse('result is null')
