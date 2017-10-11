# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from MysqldbHelper import *

# Create your views here.

def index(request):

    return render_to_response('tools.html')




