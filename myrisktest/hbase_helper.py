#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'bill'
# create on 2017/10/10
import struct
import sys

from starbase import Connection
import hbase_conf

reload(sys)
sys.setdefaultencoding('utf8')

table_info = (
    ('zhiMa_data', ['f:creditScore', 'f:creditAntifraudScore', 'f:watchList', 'f:creditAntifraudVerify',
                    'f:creditAntifraudRiskList']),
    ('weCash_data', ['f:data']),
    ('td_data', ['f:data']),
    ('rong360', ['f:xgscore', 'f:report', 'f:XGReport', 'f:baidublacklist']),
    ('AppListSummary',
     ['ALS:ALIPAY', 'ALS:CREDIT', 'ALS:DIDID', 'ALS:DIDIP', 'ALS:GAMBLE', 'ALS:LOAN', 'ALS:SZZC', 'ALS:WECHAT',
      'ALS:ZHIHU'])
)

class HbaseClient:
    #
    def __init__(self):
        self.connection = Connection(host=hbase_conf.hbase_host, port=hbase_conf.hbase_port)

    def table_list(self):
        self.connection.tables()

    def set_current_table(self, table_name):
        self.table_name = table_name
        self.current_table = self.connection.table(self.table_name)

    # 删除表
    def table_drop(self, table_name):
        self.table_name = table_name
        self.current_table = self.connection.table(self.table_name)
        self.current_table.drop()
        return True

    # 创建表
    def table_create(self, table_name, column):
        self.table_name = table_name
        self.current_table = self.connection.table(self.table_name)
        self.current_table.create(column)
        return True

    # columns_qualifiers_list : "f:xxx" ,("f:xxx","f:zzz") ,["f:xxx","f:zzz"]
    # 返回字典
    def fetch(self, row_key, columns_qualifiers_list=None):
        result = {}
        if row_key is not None:
            if columns_qualifiers_list is None:
                result = self.current_table.fetch(row_key, perfect_dict=False)
            else:
                result = self.current_table.fetch(row_key, columns=columns_qualifiers_list, perfect_dict=False)
        if result is None:
            return {}
        return result

        # 返回字符串或者None

    def fetch_one_qualifier(self, row_key, columns_qualifiers):
        if isinstance(columns_qualifiers, str) is False:
            return None
        return self.fetch(row_key, columns_qualifiers).get(columns_qualifiers, None)

    def remove(self, row_key, column=None, qualifier=None):
        if row_key is None:
            return False
        elif column is None:
            result = self.current_table.remove(row_key)
        elif qualifier is None:
            result = self.current_table.remove(row_key, column)
        else:
            result = self.current_table.remove(row_key, column, qualifier)

        if result == 200:
            return True
        else:
            return False

    def insert(self, row_key, column, qualifier, value):
        if row_key is None or column is None or qualifier is None:
            return False
        value_dict = {'%s:%s' % (column, qualifier): value}
        result = self.current_table.insert(row_key, value_dict)
        if result == 200:
            return True
        else:
            return False

    def increase(self, row_key, column, qualifier, num):
        if row_key is None or column is None or qualifier is None:
            return 0
        column_qualifier = '%s:%s' % (column, qualifier)
        old_num = struct.unpack('>Q', bytes(self.fetch(row_key, column_qualifier)[column_qualifier]))[0]
        new_num = old_num + num
        self.insert(row_key, column, qualifier, struct.pack('>Q', new_num))
        return new_num


if __name__ == '__main__':
    client = HbaseClient()