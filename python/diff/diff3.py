#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 修改有返回值的类型,可以过滤一些不比较的key值
import json
import io
import sys


class  Diff():
    def __init__(self):
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        self.d = 0  # 判断是否有不一样的 这里定义的是全局的
        self.resa=''
        self.resb=''


    # [{},{}]格式时是否排序的判断
    # def ifpaixu(self, temp, j1, j2):
    #     list1 = []
    #     list2 = []
    #     flag = 0
    #     for i in range(len(j1)):
    #         list1.append(str(j1[i].get(temp)))
    #         list2.append(str(j2[i].get(temp)))
    #     list1.sort()
    #     list2.sort()
    #     for i in range(len(list1)):
    #         if list1[i] != list2[i]:
    #             flag = 1
    #     return flag

    def diff(self,j1, j2,kwargs):
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
                    if key == 'uuid' or  key =='ImgUrl' or  key =='timestamp'or  key =='realTime'or  key =='proImg' \
                        or  key =='time' or  key =='updateTime' or key == 'TIME_STAMP' or key == 'ELAPSED_TIME':
                      continue

                    flag = 0
                    for i in kwargs:
                        if key == i:
                            flag = 1
                            break
                    if flag == 1:
                        continue

                    #   if key == 'cur_filter' or key == 'cur_filter_batch':  #对"{}"和 "[{}]"形式的特殊处理
                    #         j1[key] = json.loads(j1[key])
                    #         j2[key] = json.loads(j2[key])
                    j1[key], j2[key]= self.diff(j1[key], j2[key],kwargs)


        elif isinstance(j1, (tuple, list)) and isinstance(j2, (tuple, list)):
            #j1.sort()
            #j2.sort()
            if len(j1) != len(j2): # 直接不相等是直接涂
                j1="ThisIdYellowBegin" + str(j1) + "ThisIdYellowEnd"
                j2="ThisIdYellowBegin" + str(j2) + "ThisIdYellowEnd"
                self.d = 1
                return  j1,j2
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
                    j1[i], j2[i] = self.diff(j1[i], j2[i],kwargs)

                # if count == 1 :
                #     return  False
                #    #只有末级判断才能returm  True
                # else:
                # return  False

        elif (isinstance(j1, (int, float)) and isinstance(j2, (int, float))):
            if (abs(j1 - j2) < 0.000001 or str(j1) == str(j2)):
                return j1,j2
            else:
                j1="ThisIdYellowBegin" + str(j1) + "ThisIdYellowEnd"
                j2="ThisIdYellowBegin" + str(j2) + "ThisIdYellowEnd"
                self.d =1
                return j1, j2

        else:
            if (str(j1).find('img10.360buyimg.com')>=0 and str(j2).find('img10.360buyimg.com')>=0) or (str(j1).find('item.jd.com')>=0 and str(j2).find('item.jd.com')>=0):
                return j1, j2
            elif j1 != j2:
                if j1[0] in ['{' ,'[']:
                    #  若是"{}"和 "[{}]"形式的字符串需特殊处理
                    try:
                        j1 = json.loads(j1)  # 这里一次就好
                        j2 = json.loads(j2)
                        j1, j2 = self.diff(j1, j2,kwargs)


                    except Exception as e:
                        pass


                else:
                    j1="ThisIdYellowBegin" + j1 + "ThisIdYellowEnd"
                    j2="ThisIdYellowBegin" + j2 + "ThisIdYellowEnd"
                    self.d = 1
                    return j1, j2
            else:
                return  j1, j2
        self.resa=j1
        self.resb=j2
        return j1, j2

    def  result(self):
        if self.d:
            return True,self.resa,self.resb
        else:
            return False,self.resa,self.resb

if __name__=='__main__':
    # '{"department_5":"4339"}' 这中格式有问题呢,如果有不一致的没有标黄
    # app1={'cur_filter': {"department_5":"abc"}}
    # app2={'cur_filter': {"department_5":"abcd"}}
    # app1={'cur_filter': {"department_5":123}}
    # app2={'cur_filter': {"department_5":1234}}
    app1={'cur_filter': '[{"department_5":"4339","department_6":"433991"}]'}
    app2={'cur_filter': '[{"department_6":"433999","department_5":"43391"}]'}
    #app1={'cur_filter': '{"department_5":"3649"}'}
    #app2={'cur_filter': '{"department_5":"3648"}'}
    # app3 = {'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"3648\',\'4339","department_erp":"bjhjinj"}]'}
    # app4 = {'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"bjhjinj"}]'}
    # app1 = {'test':'abc'}
    # app2 = {'test':'abcd'}
    dif=Diff()
    dif.diff(app1,app2,['department_6'])
    # app3=json.dumps(app11)
    # print(app3)
    # app4=json.dumps(app22)
    # print(app4)
    result_diff = dif.result()
    print(result_diff)
