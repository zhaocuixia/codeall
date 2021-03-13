#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 默认修改在list/dict
# 但因为'{}'内部修改完返不回去，所以做了改良
import json
import io
import sys


class  Diff():
    def __init__(self):
        self.d = 0
        self.f = 0
        self.resa=''
        self.resb=''
        self.tag = 0  # 改良

    # [{},{}]格式时是否排序的判断
    def ifpaixu(self, temp, j1, j2):
        list1 = []
        list2 = []
        flag = 0
        for i in range(len(j1)):
            list1.append(str(j1[i].get(temp)))
            list2.append(str(j2[i].get(temp)))
        list1.sort()
        list2.sort()
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                flag = 1
        return flag

    def diff(self,j1, j2):
        if isinstance(j1, dict) and isinstance(j2, dict):
            # for key in j2.keys():
            #     if key not in j1:
            #         #print("j2中有" + key)
            #         oldkey = key
            #         newkey = "ThisIdPinkBegin%sThisIdPinkEnd"% key
            #         j2[newkey]=j2.pop(oldkey)
            #         #print('j2=%s' % j2)
            #         self.d = 1
            #print('j2=%s'%j2)

            for key in j1.keys():
                if key not in j2:
                    pass
                    # #print("j1中有" + key)
                    # oldkey = key
                    # # newkey = '<span style="background:red;">%s</span>' % key
                    # newkey = "ThisIdPinkBegin%sThisIdPinkEnd"% key
                    # j1[newkey] = j1.pop(oldkey)
                    # #print(j1[newkey])
                    # self.d = 1
                else:
                    # if key == 'uuid' or  key =='ImgUrl' or  key =='timestamp'or  key =='realTime'or  key =='proImg' \
                    #     or  key =='time' or  key =='updateTime' or key == 'TIME_STAMP' or key == 'ELAPSED_TIME':
                    #   continue
                    self.f = 0
                    self.tag = 0
                    #   if key == 'cur_filter' or key == 'cur_filter_batch':  #对"{}"和 "[{}]"形式的特殊处理
                    #         j1[key] = json.loads(j1[key])
                    #         j2[key] = json.loads(j2[key])
                    res = self.diff(j1[key], j2[key])
                    if res is True:
                        if self.f == 1:
                            j1[key] = "ThisIdYellowBegin" + str(j1[key]) + "ThisIdYellowEnd"
                            j2[key] = "ThisIdYellowBegin" + str(j2[key]) + "ThisIdYellowEnd"
                        self.d = 1
                    else:
                        if self.tag:
                            j1[key] = "ThisIdYellowBegin" + str(j1[key]) + "ThisIdYellowEnd"
                            j2[key] = "ThisIdYellowBegin" + str(j2[key]) + "ThisIdYellowEnd"

        elif isinstance(j1, (tuple, list)) and isinstance(j2, (tuple, list)):
            #j1.sort()
            #j2.sort()
            if len(j1) != len(j2): # 直接不相等是直接涂
                self.f = 1
                # j1 = '<span style="background:yellow;">' + str(j1) + '</span>'
                # j2 = '<span style="background:yellow;">' + str(j2) + '</span>'
                self.d = 1
                return  True
            else:
                count = 0
                # 若list中是dict,则diff前进行下排序
                # if len(j1) > 1:
                #     if isinstance(j1[0], dict) and isinstance(j2[0], dict):
                #         if "base_plant" in j1[0].keys() and "base_plant" in j2[0].keys() and j1[0].get("base_plant") != j1[1].get("base_plant"):
                #
                #             if self.ifpaixu("base_plant", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("base_plant")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("base_plant")), reverse=False)
                #             else:
                #                 pass
                #         elif "cur_index" in j1[0].keys() and "cur_index" in j2[0].keys() and j1[0].get('cur_index') != j1[1].get('cur_index'):
                #             if self.ifpaixu("cur_index", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("cur_index")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("cur_index")), reverse=False)
                #             else:
                #                 pass
                #         elif "key" in j1[0].keys() and "key" in j2[0].keys() and j1[0].get("key") != j1[1].get("key"):
                #             if self.ifpaixu("key", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("key")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("key")), reverse=False)
                #             else:
                #                 pass
                #
                #         elif "x" in j1[0].keys() and "x" in j2[0].keys() and j1[0].get("x") != j1[1].get("x"):
                #             if self.ifpaixu("x", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("x")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("x")), reverse=False)
                #             else:
                #                 pass
                #         elif "c_id" in j1[0].keys() and "c_id" in j2[0].keys() and j1[0].get("c_id") != j1[1].get("c_id"):
                #             if self.ifpaixu("c_id", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("c_id")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("c_id")), reverse=False)
                #             else:
                #                 pass
                #         elif "department_1" in j1[0].keys() and "department_1" in j2[0].keys() and j1[0].get("department_1") != j1[1].get("department_1"):
                #             if self.ifpaixu("department_1", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("department_1")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("department_1")), reverse=False)
                #             else:
                #                 pass
                #         elif "category_1" in j1[0].keys() and "category_1" in j2[0].keys() and j1[0].get("category_1") != j1[1].get("category_1"):
                #             if self.ifpaixu("category_1", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("category_1")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("category_1")), reverse=False)
                #             else:
                #                 pass
                #         elif "owner-pop" in j1[0].keys() and "owner-pop" in j2[0].keys() and j1[0].get("owner-pop") != j1[1].get("owner-pop"):
                #             if self.ifpaixu("owner-pop", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("owner-pop")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("owner-pop")), reverse=False)
                #             else:
                #                 pass
                #         elif "bc_business" in j1[0].keys() and "bc_business" in j2[0].keys() and j1[0].get("bc_business") != j1[1].get("bc_business"):
                #             if self.ifpaixu("bc_business", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("bc_business")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("bc_business")), reverse=False)
                #             else:
                #                 pass
                #         elif "brand" in j1[0].keys() and "brand" in j2[0].keys() and j1[0].get("brand") != j1[1].get("brand"):
                #             if self.ifpaixu("brand", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("brand")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("brand")), reverse=False)
                #             else:
                #                 pass
                #         elif "shop" in j1[0].keys() and "shop" in j2[0].keys() and j1[0].get("shop") != j1[1].get("shop"):
                #             if self.ifpaixu("shop", j1, j2) == 0:
                #                 j1 = sorted(j1, key=lambda e: str(e.get("shop")), reverse=False)
                #                 j2 = sorted(j2, key=lambda e: str(e.get("shop")), reverse=False)
                #             else:
                #                 pass
                #         else:
                #             pass

                for i in range(0, len(j1)):
                    self.f = 0
                    res = self.diff(j1[i], j2[i])
                    if res is True:
                        if self.f == 1:
                            j1[i]="ThisIdYellowBegin" + str(j1[i]) + "ThisIdYellowEnd"
                            j2[i]="ThisIdYellowBegin" + str(j2[i]) + "ThisIdYellowEnd"
                        self.d = 1
                        count=1
                    else:
                        pass

        elif (isinstance(j1, (int, float)) and isinstance(j2, (int, float))):
            if (abs(j1 - j2) < 0.000001 or str(j1) == str(j2)):
                return False
            else:
                self.d = 1
                self.f = 1
                return True

        else:
            if (str(j1).find('img10.360buyimg.com')>=0 and str(j2).find('img10.360buyimg.com')>=0) or (str(j1).find('item.jd.com')>=0 and str(j2).find('item.jd.com')>=0):
                return False
            elif j1 != j2:
                if j1[0] in ['{' ,'[']:
                    #  若是"{}"和 "[{}]"形式的字符串需特殊处理
                    try:
                        j1 = json.loads(j1)  # 这里一次就好
                        j2 = json.loads(j2)
                        res = self.diff(j1, j2)
                        self.tag = 1
                        if res is True:
                            if self.f == 1:
                                j1="ThisIdYellowBegin" + str(j1) + "ThisIdYellowEnd"
                                j2="ThisIdYellowBegin" + str(j2) + "ThisIdYellowEnd"
                            self.d = 1
                            return False

                    except Exception as e:
                        self.d = 1
                        self.f = 1

                else:
                    self.d = 1
                    self.f = 1
                    return True

            else:
                return  False
        self.resa=j1
        self.resb=j2
        return  False
    
    def  result(self):
        if self.d == 1:
            return True,self.resa,self.resb
        else:
            return False,self.resa,self.resb

if __name__=='__main__':
    # '{"department_5":"4339"}' 这中格式有问题呢,如果有不一致的没有标黄
    app1={'cur_filter': {"department_5":"43392","department_6":"43399"}}
    app2={'cur_filter': {"department_6":"433993","department_5":"4339"}}
    # app1={'cur_filter': '{"department_5":"3649"}'}  #
    # app2={'cur_filter': '{"department_5":"3648"}'}
    # app11 ={'status': 1, 'time_msg': '', 'err_msg': '', 'SYSTEM_DEBUG': {'ELAPSED_TIME': 329.66186523438, 'TIME_STAMP': 1615258985}, 'data': {'cur_categorys': 'department_1,department,department_3,department_4,department_5,department_erp,brand', 'next_category_list': [{'name': '平台', 'is_no_avg': 1, 'key': 'department_1,department,department_3,department_4,department_5,department_erp,brand,platform'}], 'unit': '万', 'list': [{'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '10.5'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}], 'is_bottom': 1, 'name': '汇总', 'key': 'summary'}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"7046"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '5.03'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '芙丽芳丝（Freeplus）', 'key': 7046}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"80044"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '3.94'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '珂润（Curel）', 'key': 80044}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"8464"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '1.07'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '花印（HANAJIRUSHI）', 'key': 8464}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"627939"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.213'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '皑丽（ALLIE）', 'key': 627939}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"182432"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.177'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'DR.G', 'key': 182432}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"164911"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.145'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'Loshi', 'key': 164911}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"104557"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.142'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '蜜浓（MINON）', 'key': 104557}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"161221"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.139'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '怡思丁（ISDIN）', 'key': 161221}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"71302"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0462'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '柳屋', 'key': 71302}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"168669"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0069'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'ABOUT ME', 'key': 168669}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"4609"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0045'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '贝佳斯（Borghese）', 'key': 4609}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"14261"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0021'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '千妇恋（CHIFURE）', 'key': 14261}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"283614"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0014'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'repavar', 'key': 283614}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"118826"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0004'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '杜碧丝（Dimples）', 'key': 118826}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"395490"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0004'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '妮珍', 'key': 395490}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"471127"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0003'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '好优可（NICE QUICK）', 'key': 471127}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"7293"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0003'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '高丽雅娜（Coreana）', 'key': 7293}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"260989"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '玥之秘', 'key': 260989}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"442604"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '怡婷美', 'key': 442604}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"526982"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'KOSMEA', 'key': 526982}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"197964"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'Elta MD', 'key': 197964}]}}
    # app22 ={'status': 1, 'time_msg': '', 'err_msg': '', 'SYSTEM_DEBUG': {'ELAPSED_TIME': 234.65380859375, 'TIME_STAMP': 1615258986}, 'data': {'cur_categorys': 'department_1,department,department_3,department_4,department_5,department_erp,brand', 'next_category_list': [{'name': '平台', 'is_no_avg': 1, 'key': 'department_1,department,department_3,department_4,department_5,department_erp,brand,platform'}], 'unit': '万', 'list': [{'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_erp":"bjhjinj","department_1":"1726","department":"2785","department_3":"3626","department_4":"3647\',\'4338","department_5":"3648\',\'4339"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '10.5'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}], 'is_bottom': 1, 'name': '汇总', 'key': 'summary'}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"7046"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '5.03'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '芙丽芳丝（Freeplus）', 'key': 7046}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"80044"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '3.94'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '珂润（Curel）', 'key': 80044}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"8464"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '1.07'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '花印（HANAJIRUSHI）', 'key': 8464}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"627939"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.213'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '皑丽（ALLIE）', 'key': 627939}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"182432"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.177'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'DR.G', 'key': 182432}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"164911"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.145'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'Loshi', 'key': 164911}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"104557"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.142'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '蜜浓（MINON）', 'key': 104557}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"161221"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.139'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '怡思丁（ISDIN）', 'key': 161221}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"71302"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0462'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '柳屋', 'key': 71302}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"168669"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0069'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'ABOUT ME', 'key': 168669}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"4609"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0045'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '贝佳斯（Borghese）', 'key': 4609}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"14261"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0021'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '千妇恋（CHIFURE）', 'key': 14261}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"283614"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0014'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'repavar', 'key': 283614}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"118826"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0004'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '杜碧丝（Dimples）', 'key': 118826}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"395490"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0004'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '妮珍', 'key': 395490}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"471127"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0003'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '好优可（NICE QUICK）', 'key': 471127}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"7293"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0003'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '高丽雅娜（Coreana）', 'key': 7293}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"260989"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '玥之秘', 'key': 260989}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"442604"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': '怡婷美', 'key': 442604}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"3647","department_5":"3648","department_erp":"bjhjinj","brand":"526982"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'KOSMEA', 'key': 526982}, {'graph_tab': [{'name': '十分', 'key': 'slot'}, {'name': '小时', 'key': 'hour'}], 'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj","brand":"197964"}]', 'rows': [{'base_plant': 'global', 'c_name': '胡金晶', 'pre_year_data': '-', 'pre_year_uptick': '-', 'today': '0.0001'}], 'cur_index': 'detail_uv', 'operation_tab': [{'name': '邮件推送指标', 'key': 'send_email', 'is_fold': '1'}, {'name': '指标概览', 'key': 'index_list', 'is_fold': '1'}], 'is_bottom': 0, 'name': 'Elta MD', 'key': 197964}]}}
    # # app3 = {'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"3648\',\'4339","department_erp":"bjhjinj"}]'}
    # app4 = {'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj"}]'}
    # app11 = {'test':'123'}
    # app22 = {'test':'123'}
    dif=Diff()
    dif.diff(app1,app2)
    # app3=json.dumps(app11)
    # print(app3)
    # app4=json.dumps(app22)
    # print(app4)
    result_diff = dif.result()
    print(result_diff)
