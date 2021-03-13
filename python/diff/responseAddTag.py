#  对请求返回值做处理，加"ThisIdYellowBegin" ，"ThisIdYellowEnd"
#  注意对最后一层的修改如果是不可变类型（string，int）返回上一级是不会修改的，除非有修改的返回值
#  对list，dict的修改返回上一层也是修改的结果

import json
#  有返回值的修改
def test2(temp):
    if isinstance(temp, dict):
        for key in temp.keys():
            temp[key] = test2(temp[key])
    elif isinstance(temp, (list, tuple)):
        for i in range(0, len(temp)):
            temp[i] = test2(temp[i])
    elif isinstance(temp, str):
        if temp[0] in ['{', '[']:
            temp = json.loads(temp)
            temp = test2(temp)
        else:
            temp = "ThisIdYellowBegin" + temp + "ThisIdYellowEnd"
    elif isinstance(temp, int):
        temp  = "ThisIdYellowBegin" + str(temp) + "ThisIdYellowEnd"
    else:
        pass
    return temp  # 注意递归的每次都有return返回上层


# 原因解释：最底层的修改，没有返回上一层；是不是因为底层是不可变数据类型,可变类型是适用的
def test3(temp):
    if isinstance(temp, dict):
        for key in temp.keys():
            res = test3(temp[key])
    elif isinstance(temp, (list,tuple)):
        for i in range(0, len(temp)):
            res = test3(temp[i])
    elif isinstance(temp, str):
        if temp[0] in ['{' ,'[']: # 加判断
            res =json.loads(temp)
            test3(temp)
        else:
            temp="ThisIdYellowBegin" + temp + "ThisIdYellowEnd"
    elif isinstance(temp, int):
        temp="ThisIdYellowBegin" + str(temp) + "ThisIdYellowEnd"
    else:
        pass

    return False

if __name__=='__main__':
    # temp = {'cur_filter': 123}
    temp = {'cur_filter': '123'}
    # temp = {'cur_filter': '{"department_5":"4339","department_6":"43399"}'}
    # temp = {'cur_filter': {"department_5":"4339","department_6":"43399"}}
    # temp = {'cur_filter': [{"department_5":"4339","department_6":"43399"}]}
    # temp = {'cur_filter': '[{"department_1":"1726","department":"2785","department_3":"3626","department_4":"4338","department_5":"4339","department_erp":"abc"}]'}
    # temp={'cur_filter': {"department_6":"43399","department_5":"4339"}}
    # ans = test(temp)
    # print(ans)
    test3(temp)
    print(temp)
