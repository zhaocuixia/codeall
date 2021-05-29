#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime
import sys
import os
from urllib.parse import urlencode

class Log_filer(object):

    def __init__(self):
        # self.exclude_g = ['email_view', 'permission']
        self.exclude_params = ['timestamp', 'uniq_id', 'os_plant', 'net_type', 'version', 'language']
        self.white_list_c = ['core_view', 'thematic_view', 'panoramic_view', 'industry_view']
        self.TOKEN = 'tester:xxx'
        self.jmeter_url_file = 'app_urls_jmeter.txt'
        self.gor_url_file = 'app_urls_gor.gor'
        self.diff_url_file = 'app_urls_diff.txt'
        self.init_param = 'autoTest'
        self.forcebot_url_file='app_url_forcebot.gor'
        self.forcebot_http_file = 'app_url_forcebot_http.txt'

    def get_gca(self, param_dict):
        #flag用来标识此条日志是否保留，如果没有gc参数，就不保留
        flag = False
        url_param = ''
        keys = param_dict.keys()
        # url参数中的g、c、a
        url_param_list = list()
        # 将gca参数单独取出来
        if 'g' in keys:
            if param_dict['g'] is not '':
                url_param_list.append('g={}'.format(param_dict['g']))
                param_dict.pop('g')
                flag = True

        if 'c' in keys:
            if param_dict['c'] is not '' and param_dict['c'] in self.white_list_c:
                url_param_list.append('c={}'.format(param_dict['c']))
                param_dict.pop('c')
                flag = True
            else:
                flag = False
        else:
            flag = False

        if 'a' in keys:
            if param_dict['a'] is not '':
                url_param_list.append('a={}'.format(param_dict['a']))
                param_dict.pop('a')

        if len(url_param_list) >= 2 and flag is True:
            url_param = '&'.join(url_param_list)

        return flag, url_param, param_dict

 

    def log_filer_for_press(self, logfile, appVersion, type, host,datatype,convert_flag):
        now_date=datetime.now().strftime('%Y-%m-%d')
        if type == 'jmeter':
            fullpath = sys.path[0] + os.sep + 'urls' + os.sep + self.jmeter_url_file
        elif type == 'gor':
            fullpath = sys.path[0] + os.sep + 'urls' + os.sep + self.gor_url_file
        elif type == 'forcebot':
            fullpath = sys.path[0] + os.sep + 'urls' + os.sep + self.forcebot_url_file
        elif type == 'http':#forcebot http请求
            fullpath = sys.path[0] + os.sep + 'urls' + os.sep + self.forcebot_http_file
        else:
            print("invalid press type!!!")
            sys.exit(3)
        logfile = sys.path[0] + os.sep + 'log' + os.sep + logfile
        print('-'*100)
        print('start to process log for performance test.')
        start_time = datetime.now()
        try:
            log = open(logfile)
            fw = open(fullpath, 'w', encoding='utf-8')

            couter = 0
            counter_line = 0
            while True:
                # print(counter_line)
                # counter_line = counter_line+1
                line = log.readline()
                # print('this line is ' + line)
                if line.strip('\n') == 'null' or line.strip('\n') == '':
                    break
                if not line:
                    break
                counter_line = counter_line + 1
                print(counter_line, line)
                log_param = json.loads(line)
                erp = ''
                flag, url_param, param_dict = self.get_gca(log_param)
                data_param = ''
                data_param_list = list()

                if not flag:
                    continue
                keys = param_dict.keys()
                # 去掉不需要的接口参数
                for key in self.exclude_params:
                    if key in keys:
                        param_dict.pop(key)

                # 将历史日期的实时日志转换为当天的实时日志
                if convert_flag=='true':
                    file_date = os.path.basename(logfile)[4:0]
                    print('file_date=%s' % file_date)
                    param_dict['cur_date'] = now_date

                # 增加判断是否只过滤实时或者离线数据
                if datatype == 'realtime':
                    if 'cur_date' in keys and param_dict['cur_date'] != now_date:
                        print(param_dict['cur_date'])
                        flag = False
                if datatype == 'offline':
                    if 'cur_date' in keys and (param_dict['cur_date'] == now_date):
                        flag = False
                if not flag:
                    continue
                # 将access_user的值取出来放进token中
                if 'access_user' in keys:
                    if param_dict['access_user'] is not '' and param_dict['access_user']!='t_tester':

                        erp = param_dict['access_user']
                        param_dict['token'] = erp
                        param_dict.pop('access_user')
                    else:
                        continue
                else:
                    continue

                # 将app版本先置为4.0.0,因为此方式从400版本才开始支持
                param_dict['app_version'] = appVersion

                param_dict['t_token'] = self.TOKEN
                # 日志计入线上musql库时，需要加入sys_is_clear_text=0标记
                param_dict['sys_is_clear_text'] = 0
                for key in param_dict.keys():
                    data_param_list.append('{}={}'.format(key, param_dict[key]))  # 键与值是等号格式了

                if type == 'jmeter':
                    if len(data_param_list) > 2:
                        data_param = '&'.join(data_param_list)
                        # print(data_param)

                    if url_param is not '' and data_param is not '':
                        if couter != 0:
                            fw.write('\n')
                        fw.write('{}\t{}'.format(url_param, data_param))
                        couter += 1
                elif type == 'gor':
                    if len(data_param_list) > 2 and url_param is not '':
                        # print(self.convert_log_to_gor(url_param, host, param_dict))
                        fw.write(self.convert_log_to_gor(url_param, host, param_dict))
                elif type=='forcebot':
                    if len(data_param_list) > 2 and url_param is not '':
                        # print(self.convert_log_to_gor(url_param, host, param_dict))
                        fw.write(self.convert_log_to_forcebot_gor(url_param, host, param_dict))
                elif type=='http':
                    if len(data_param_list) > 2:
                        data_param = '&'.join(data_param_list)
                        # print(data_param)

                    if url_param is not '' and data_param is not '':
                        if couter != 0:
                            fw.write('\n')
                        fw.write('{}&{}'.format(url_param, data_param))
                        couter += 1

                couter += 1
        except Exception as e:
            print('errormessage:%s'%e)
        finally:
            fw.close()
            log.close()
        end_time = datetime.now()
        print('process log for press test done.')
        print('time use {} seconds'.format(str((end_time-start_time).seconds)))

    def convert_log_to_gor(self, url, host, param_json):
        raw_str = "1 6b7b9c43ed43a1d68d5e90fdf24d30ad6a9139c9 1586500520672120380\n" \
                  "POST /mba_test.php?{} HTTP/1.1\r\n" \
                  "Host: {}\r\n" \
                  "User-Agent: python-requests/2.19.1\r\n" \
                  "Accept-Encoding: gzip, deflate\r\n" \
                  "Accept: */*\r\n" \
                  "Connection: close\r\n" \
                  "Content-Length: {}\r\n" \
                  "Content-Type: application/x-www-form-urlencoded\r\n\r\n" \
                  "{}\n" \
                  "🐵🙈🙉" \
                  "\n"

        body_value = urlencode(param_json)
        bogy_len = len(body_value)
        body_content = raw_str.format(url, host, bogy_len, body_value)
        return body_content

    def convert_log_to_forcebot_gor(self, url, host, param_json):
        raw_str = "1 6b7b9c43ed43a1d68d5e90fdf24d30ad6a9139c9 1586500520672120380\n" \
                  "POST /mba_test.php?{}&forcebot=1 HTTP/1.1\r\n" \
                  "Host: {}\r\n" \
                  "User-Agent: python-requests/2.19.1\r\n" \
                  "Accept-Encoding: gzip, deflate\r\n" \
                  "Accept: */*\r\n" \
                  "Connection: close\r\n" \
                  "Content-Length: {}\r\n" \
                  "Content-Type: application/x-www-form-urlencoded\r\n\r\n" \
                  "{}\n" \
                  "🐵🙈🙉" \
                  "\n"

        body_value = urlencode(param_json)
        bogy_len = len(body_value)
        body_content = raw_str.format(url, host, bogy_len, body_value)
        return body_content

   

if __name__ == '__main__':
    logFilter = Log_filer()
    filepath = 'log-05-08.txt'
    #logFilter.log_filer_for_press('log-2020-05-09.txt','4.0.0', 'gor', 'ge.m.jd.com.local', 'realtime',True)
#     # logFilter.log_filter('mylog.txt')
#     # logFilter.log_filer_for_press('log-all-0303.txt')
    #filepath=os.getcwd() + os.sep +'log'+os.sep+'log-2020-05-09.txt'
    logFilter.log_filter_for_diff(filepath)


    

