# -*- coding: utf-8 -*-


from django.http import HttpResponse
import os,sys

def autoreportlist(request):
    path = '/apps/data/act/autoreport'
    #  path = '/Users/zhouyahui/code/hhht/static/report'
    reporturl = 'http://119.23.218.196:7081/autoreport'
    reportlist = []
    for file in os.listdir(path):
        reportlist.append("filename=%s,url=%s%s;" % \
                        (file,reporturl,file))
        print file
        return HttpResponse(reportlist)
