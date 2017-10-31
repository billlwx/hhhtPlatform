# -*- coding: utf-8 -*-


from django.http import HttpResponse
import os,sys

def autoreportlist(request):
    path = '/apps/data/act/autoreport/'
    # # path = '/Users/zhouyahui/code/hhht/static/report'
    # f_list = os.listdir(path)
    reporturl = 'http://119.23.218.196:7081/'
    reportlist = []
    for filenames in os.walk(path):
        for filename in filenames:
            reportlist.append("filename=%s,url=%s+%s;" % \
                        (filename,reporturl,filename))
            return HttpResponse(reportlist)
