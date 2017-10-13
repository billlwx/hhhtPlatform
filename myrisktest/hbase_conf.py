#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/10
import sys
import env_conf

reload(sys)
sys.setdefaultencoding('utf8')

# see wiki
if env_conf.env == env_conf.env_dict['cgg_test']:
    hbase_host = '172.18.225.180'
    hbase_port = '8080'

if env_conf.env == env_conf.env_dict['dxq_test']:
    hbase_host = '172.18.225.199'
    hbase_port = '50056'