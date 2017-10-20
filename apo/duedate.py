#-*- coding: UTF-8 -*-
from MysqldbHelper import *
from django.http import HttpResponse
from zidian import *
import datetime
import time
import random


def duedate(request):
    db = DB(**cgg_test_db)
    sign = request.GET['usersign']
    tm = str(time.time())
    select = 'select * from '
    shuiji = str(random.randint(0,99))
    contract_no = sign + tm + shuiji

    dateArray = datetime.datetime.now()
    datenow = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    repay_yes_time =(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")

    contractsql = "INSERT INTO `contract` (`uid`, `contract_no`, `partner`, `channel`, `product_code`, `apply_amount`, `credit_amount`, `real_amount`, `duration`, `service_fee_rate`, `late_interest_rate`, `late_fine_rate`, `service_fee`, `interest`, `start_time`, `finish_time`, `total_yes_amount`, `total_no_amount`, `repay_yes_time`, `last_repay_time`, `late_day`, `late_status`, `status`, `name`, `identity_card`, `phone`, `bank_card`, `bank`, `cur_period`, `app_name`, `app_version`, `created_by`, `last_modified_by`, `created_date`, `last_modified_date`, `case_no`, `reg_dist_channel`, `reg_promo_activity`, `reg_promo_channel`, `signature_url`, `reject_code`, `reject_msg`, `market`, `bus_name_code`, `valid_time`) VALUES ('136249','%s', '', 'APP', '00004', '10.00', '10.00', '10.00', '14', '0.0490000000', '0.0000000000', '0.0300000000', '0.49', '0.0006000000', '%s', '%s', '0.00', '20.55', NULL, '%s', '1', 'OVERDUE', 'HAVE_LOAN', '测试', '421023199004070765', '18310709835', '622700*********7698', '建设银行', '1', 'cgg_android', '2.3.0', '136249', 'scheduler', '%s', '%s', '10480', 'haohan_channel', 'SJ01', 'AA004', '', '', '', '0', '100001', '%s')" % (contract_no,datenow,datenow,repay_yes_time,datenow,datenow,datenow)

    selectcollection_no = 'select collection_no from overdue_collection ORDER BY collection_no desc  limit 1'
    oldcolno = db.query(selectcollection_no)
    collection_no = oldcolno+1
    overdue_collection = "INSERT INTO `overdue_collection` (`collection_no`, `contract_no`, `case_no`, `collection_status`, `collector`, `assign_status`, `assign_time`, `loan_count`, `overdue_days`, `late_interest`, `overdue_interest`, `communicate_comment`, `communicate_result`, `created_by`, `last_modified_by`, `created_date`, `last_modified_date`, `collector_id`) VALUES ('%s', '%s', '10480', '0', NULL, '0', '1980-01-01 00:00:00', '21', '1', '0.00', '10.00', NULL, NULL, NULL, NULL, '%s', '%s', NULL)" % (collection_no,contract_no,datenow,datenow)

    db.update(contractsql)
    db.update(overdue_collection)
    return HttpResponse("success")