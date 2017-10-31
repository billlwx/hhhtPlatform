# -*- coding: utf-8 -*-


from django.http import HttpResponse
import os,sys
import json

def autoreportlist(request):
    path = '/apps/data/act/autoreport'
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
        HttpResponse(json.dumps(reportlist, ensure_ascii=False))

    else:
        return HttpResponse('result is null')
