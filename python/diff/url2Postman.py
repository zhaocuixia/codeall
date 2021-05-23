#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import sys
import getopt

yf_url = 'http://xxx.php?'
online_url = 'http:/xxx.php?'
TOKEN = 'tester:xxx'
online_version = '4.1.9'
yf_version = '4.1.9'
param1 = 'g=core_view&c=core_view&a=getCoreSum'
param2 = "{'t_type': 't1', 'method': 'getCoreSum', 'mode': '', 'app_version': '4.2.0', 'cur_dimens': 'pre_year_data,pre_year_uptick', 'cur_dimens_start_date': '2021-03-08', 'token': 'wangjingjing100', 'cur_aspect': 'order', 'bc_type': '', 'index_type': '', 'cur_start_date': '2021-03-10', 'cur_dimens_date': '2021-03-14', 'app_build': '210228001', 'holiday_id': '', 'evil_type': '', 'category_key': 'wangjingjing100', 'cur_dimens_end_date': '2021-03-14', 'category_type': 'department_erp', 'cur_end_date': '2021-03-16', 'sale_role': 'seller', 'cur_date': '2021-03-16', 'is_avg_per_day': '0', 'date_type': 'day', 'base_plant': '', 'holiday_type': ''}"
param2 = param2[2:-2]
yf_url = yf_url + param1
#print(yf_url)
online_url = online_url + param1
#print(online_url)
param2 = param2.replace('\': \'', '=')
param2 = param2.replace('\', \'', '&')
yf_url = yf_url + '&' + param2
#print(yf_url)
online_url = online_url + '&' + param2
#print(online_url)
yf_url = yf_url + '&app_version=' + yf_version + '&t_token=' + TOKEN
print("预发url")
print(yf_url, end='')
print('\n')
online_url = online_url + '&app_version=' + online_version + '&t_token=' + TOKEN
print("线上url")
print(online_url, end='')
print('\n')

