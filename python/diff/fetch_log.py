#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import sys
import os
from datetime import datetime, timedelta
from math import ceil
import getopt


class FetchLog(object):

    def __init__(self):
        self.HOST = 'gateht3b.jed.jddb.com'
        self.PORT = 3358
        self.USERNAME = 'ge_log_rr'
        self.PASSWORD = 'YMNkIhx59aLr1Jke'
        self.DATABASE = 'ge_log'
        self.TABLE = 'ge_user_fore_access_log'
        self.FILENAME = 'log.txt'
        self.logDateStart=None
        self.logDateEnd=None
        self.filter=None
        self.start_time=None
        self.end_time=None

    def __getparam__(self,argv):
        helpStr = '{} -d <startdate> -D <enddate> -f <filter> -s <start_time> -e <end_time>'.format(argv[0])

        try:
            opts, args = getopt.getopt(argv[1:], "hd:D:f:s:e:",["startdate=", "enddate=", "filter=", "start_time=", "end_time="])
        except getopt.GetoptError:
            print(helpStr)
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print(helpStr)
                sys.exit()
            elif opt in ("-d", "--startdate"):
                self.logDateStart = arg
            elif opt in ("-D", "--enddate"):
                self.logDateEnd = arg
            elif opt in ("-f", "--filter"):
                self.filter = arg
                print (self.filter)
            elif opt in ("-s", "--start_time"):
                self.start_time = arg
            elif opt in ("-e", "--end_time"):
                self.end_time=arg
            else:
                print('Unrecognized paramters')
                print(helpStr)
                sys.exit(3)

    def get_log_from_db(self, argv):
        self.__getparam__(argv)
        logDate = (datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d')
        logDateStart = logDate
        logDateEnd = logDate
        if self.logDateStart is not None:
            logDateStart = self.logDateStart
            if self.logDateEnd is not None:
                logDateEnd = self.logDateEnd  # 开始结束日期都不为空
            else:
                logDateEnd = self.logDateStart  # 开始日期都不为空,结束日期为空
        else:
            if self.logDateEnd is not None:
                logDateEnd = self.logDateEnd  # 开始日期为空，结束日期都不为空
                logDateStart = self.logDateEnd
            else:
                pass  # 开始结束日期都为空
                    
        filepath = sys.path[0] + os.sep + 'log' + os.sep + 'log-{}.txt'.format(logDateEnd)
        print('filepath:%s'%filepath)
        if os.path.exists(filepath):
            os.remove(filepath)

        #可以取某一天某个时间段的日志，若不填写则取全部日志
        if not self.start_time:
            start_time = '{} 00:00:00'.format(logDateStart)
        else:
            start_time='{} {}'.format(logDateStart,self.start_time)
        if not self.end_time:
            end_time = '{} 23:59:59'.format(logDateEnd)
        else:
            end_time='{} {}'.format(logDateEnd,self.end_time)

        sql_count = 'select max(log_id),min(log_id) from {} where create_time>=\'{}\' and create_time<=\'{}\''.format(self.TABLE, start_time, end_time)
        sql_get_init = 'select complete_json from {} where create_time>=\'{}\' and create_time<=\'{}\' and access_user!=\'t_tester\''.format(self.TABLE, start_time, end_time)
        print('sql_count=%s'%sql_count)
        conn = pymysql.connect(host=self.HOST, port=self.PORT, user=self.USERNAME, passwd=self.PASSWORD, db=self.DATABASE, charset='utf8')
        cur = conn.cursor()
        #查询出日志id的最大值和最小值，分批次查询并写入文件
        cur.execute(sql_count)
        rows = cur.fetchone()
        print(rows)
        max_id = rows[0]
        min_id = rows[1]
        # max_id = 2874610
        # min_id = 2833952
        count = max_id - min_id + 1
        each_num = 10000
        batch = int(ceil(count/each_num))

        start_id = min_id
        end_id = min_id

        with open(filepath, 'a') as f:
            for i in range(0, batch):
                start_id = start_id
                if i != batch - 1 and start_id < max_id:
                    end_id = start_id + each_num - 1
                else:
                    end_id = max_id
                print(start_id, end_id)
                if self.filter:
                    sql_get = '{} and log_id>={} and log_id<={} and {}'.format(sql_get_init, start_id, end_id,self.filter)
                else:
                    sql_get = '{} and log_id>={} and log_id<={}'.format(sql_get_init, start_id, end_id)
                print('sql_get:%s' % (sql_get))
                cur.execute(sql_get)
                rows = cur.fetchall()
                for row in rows:
                    f.write(str(row[0]) + '\n')

                start_id = end_id + 1
        cur.close()
        conn.close()
        #f.close()


if __name__ == '__main__':
    getLog = FetchLog()
    getLog.get_log_from_db(sys.argv)
    #getLog.get_log_from_db('2020-05-13',"sys_elapsed_time>10000 or thematic_key='7fresh' or cur_categorys in ('brand','shop') or cur_aspect = 'supply'")
    #if(len(sys.argv)>4):
    #    getLog.get_log_from_db(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    #elif(len(sys.argv)==4):
    #    getLog.get_log_from_db(sys.argv[1], sys.argv[2], sys.argv[3])
    #elif(len(sys.argv)==3):
    #    getLog.get_log_from_db(sys.argv[1], sys.argv[2])
    #elif(len(sys.argv)==2):
    #    getLog.get_log_from_db(sys.argv[1])
    #else:
    #    getLog.get_log_from_db()



