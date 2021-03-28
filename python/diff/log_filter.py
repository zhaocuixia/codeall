#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 对拉取的日志进行相关Key过滤,格式处理
import json
from datetime import datetime
import sys
import os
from urllib.parse import urlencode

class Log_filer(object):

    def __init__(self):
        self.exclude_params = ['timestamp', 'uniq_id', 'os_plant', 'net_type', 'version', 'language']
        self.white_list_c = ['core_view', 'thematic_view', 'panoramic_view', 'industry_view']
        self.TOKEN = 'tester:xxxxx'
        self.diff_url_file = 'app_urls_diff.txt'
        self.init_param = 'autoTest'

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

        return flag, url_param, param_dict   # 字符，字符，dict
    def log_filter_for_diff(self, log_file):
        now_date = datetime.now().strftime('%Y-%m-%d')
        fullpath = os.getcwd() + os.sep + self.diff_url_file
        logfile = os.getcwd() + os.sep + log_file
        print('-' * 100)
        print('start to process log for diff test.')
        start_time = datetime.now()

        log = open(logfile)
        fw = open(fullpath, 'w', encoding='utf-8')
        urls = []
        # 需要进行去重的字段
        keys_list = ['grab_tabs', 'cur_indexes', 'cur_dimenses', 'base_plants', 'holiday_types', 'cur_categoryses',
                     'category_types', 'cur_aspects']
        param_dict = dict()

        # 计数，用来避免最后生成一个空行
        counter = 0

        while True:
            param_flag = False
            line = log.readline()
            if line.strip('\n') == 'null' or line.strip('\n') == '':
                break
            if not line:
                break
            params_log = json.loads(line)
            erp = ''
            url_flag, url_param, params = self.get_gca(params_log)
            # 如果没有gc参数则跳过
            if not url_flag:
                continue

            keys = params.keys()
            # 去掉不需要的接口参数
            for key in self.exclude_params:
                if key in keys:
                    params.pop(key)

            # # 参数初始化,附一个特殊的值，各参数都会有为''的情况
            # grab_tab = self.init_param
            # cur_index = self.init_param
            # cur_dimens = self.init_param
            # base_plant = self.init_param
            # holiday_type = self.init_param
            # cur_categorys = self.init_param
            # category_type = self.init_param
            # cur_aspect = self.init_param
            # # 取出参数的值
            # if 'grab_tab' in keys:
            #     grab_tab = params['grab_tab']
            #
            # if 'cur_index' in keys:
            #     cur_index = params['cur_index']
            #
            # if 'cur_dimens' in keys:
            #     cur_dimens = params['cur_dimens']
            #
            # if 'base_plant' in keys:
            #     base_plant = params['base_plant']
            #
            # if 'cur_categorys' in keys:
            #     cur_categorys = params['cur_categorys']
            #
            # if 'category_type' in keys:
            #     category_type = params['category_type']
            #
            # if 'cur_aspect' in keys:
            #     cur_aspect = params['cur_aspect']
            #
            # if 'holiday_type' in keys:
            #     holiday_type = params['holiday_type']
            #
            # if url_param not in urls and url_param is not '':
            #     param_flag = True
            #     param_dict[url_param] = {}
            #     urls.append(url_param)
            #
            #     for key in keys_list:
            #         param_dict[url_param][key] = []
            #
            #     if grab_tab != self.init_param:
            #         param_dict[url_param]['grab_tabs'].append(grab_tab)
            #     if cur_index != self.init_param:
            #         param_dict[url_param]['cur_indexes'].append(cur_index)
            #     if cur_dimens != self.init_param:
            #         param_dict[url_param]['cur_dimenses'].append(cur_dimens)
            #     if base_plant != self.init_param:
            #         param_dict[url_param]['base_plants'].append(base_plant)
            #     if holiday_type != self.init_param:
            #         param_dict[url_param]['holiday_types'].append(holiday_type)
            #     if cur_categorys != self.init_param:
            #         param_dict[url_param]['cur_categoryses'].append(cur_categorys)
            #     if category_type != self.init_param:
            #         param_dict[url_param]['category_types'].append(category_type)
            #     if cur_aspect != self.init_param:
            #         param_dict[url_param]['cur_aspects'].append(cur_aspect)
            # elif url_param in urls:
            #     if grab_tab not in param_dict[url_param]['grab_tabs'] and grab_tab != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['grab_tabs'].append(grab_tab)
            #     if cur_index not in param_dict[url_param]['cur_indexes'] and cur_index != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['cur_indexes'].append(cur_index)
            #     if cur_dimens not in param_dict[url_param]['cur_dimenses'] and cur_dimens != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['cur_dimenses'].append(cur_dimens)
            #     if base_plant not in param_dict[url_param]['base_plants'] and base_plant != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['base_plants'].append(base_plant)
            #     if cur_categorys not in param_dict[url_param][
            #         'cur_categoryses'] and cur_categorys != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['cur_categoryses'].append(cur_categorys)
            #     if holiday_type not in param_dict[url_param]['holiday_types'] and holiday_type != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['holiday_types'].append(holiday_type)
            #     if category_type not in param_dict[url_param][
            #         'category_types'] and category_type != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['category_types'].append(category_type)
            #     if cur_aspect not in param_dict[url_param]['cur_aspects'] and cur_aspect != self.init_param:
            #         param_flag = True
            #         param_dict[url_param]['cur_aspects'].append(cur_aspect)
            # else:
            #     continue
            #
            # # 将历史日期的实时日志转换为当天的实时日志
            # #if convert_flag:
            # #    file_date = os.path.basename(logfile)[4:0]
            # #    print('file_date=%s' % file_date)
            # #    params['cur_date'] = now_date

            # 将access_user的值取出来放进token中
            if 'access_user' in keys:
                if params['access_user'] is not '' and params['access_user']!='t_tester':
                    # if params['access_user'] == 'wangnana1':
                    erp = params['access_user']
                    params['token'] = erp
                    params.pop('access_user')
                else:
                    continue
            else:
                continue

            # 将app版本先置为4.0.0,因为此方式从400版本才开始支持
            # params['app_version'] = appVersion
            # params['t_token'] = self.TOKEN

            # 先去掉版本，最终diff的时候再加上版本号
            if 'app_version' in keys:
                params.pop('app_version')

            if url_flag is True:
                if counter != 0:
                    fw.write('\n')
                fw.write(url_param + '\t')
                fw.write(json.dumps(params, ensure_ascii=False))
                counter += 1

        fw.close()
        log.close()
        end_time = datetime.now()
        print('process log for diff test done.')
        print('time use {} seconds'.format(str((end_time-start_time).seconds)))


if __name__ == '__main__':
    logFilter = Log_filer()
    filepath = 'log-2021-03-22.txt'
    #filepath=os.getcwd() + os.sep +'log'+os.sep+'log-2020-05-09.txt'
    logFilter.log_filter_for_diff(filepath)



