#!/usr/bin/python
# -*- coding: UTF-8 -*-
import traceback
# from SendRequest import SendRequest
import sys

from Diff import Diff
import json
import os
import time
import requests
import sys
import getopt


def main(argv):
    TOKEN = 'tester:xxxxxxxxxxxxx'
    filepath = 'app_urls_diff.txt'
    fullpath = sys.path[0] + os.sep + 'urls' + os.sep + filepath
    resultFile = 'test.log'
    app_version1 = ''
    app_version2 = ''

    helpStr = '{} -v <online_version> -V <yf_version> -u <online_url> -U <yf_url>'.format(argv[0])
    try:
        opts, args = getopt.getopt(argv[1:], "hv:V:u:U:", ["help","online_version=","yf_version=","online_url=","yf_url="])
        #print(opts,args)
    except getopt.GetoptError:
        #print(helpStr)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            #print(helpStr)
            sys.exit()
        #elif opt in ("-f", "--logFileName"):
        #    filepath = arg
        elif opt in ("-v", "--appVersion1"):
            online_version = arg
            #print(online_version)
        elif opt in ("-V", "--appVersion2"):
            yf_version = arg
            #print(yf_version)
        elif opt in ("-u","--online_url"):
            online_url=arg
            #print('online_url=%s'%online_url)
        elif opt in ("-U","--yf_url"):
            yf_url=arg
            #print('yf_url=%s'%yf_url)
        else:
            print('Unrecognized paramters')
            print(helpStr)
            sys.exit(3)


    try:
        fw = open(resultFile, 'w', encoding='utf-8')
        f = open(fullpath)
        counter = 0
        while True:
            #if counter > 10:
            #    break
            line = f.readline()
            if not line:
                break
            line_param = line.strip('\n').split('\t')
            url1 = online_url + line_param[0]
            url2 = yf_url + line_param[0]
            param_body1 = json.loads(line_param[1])
            param_body2 = json.loads(line_param[1])
            param_body1['app_version'] = online_version
            param_body2['app_version'] = yf_version
            param_body1['t_token'] = TOKEN
            param_body2['t_token'] = TOKEN

            try:
                # resA = str(requests.post(url1, data=param_body).text)
                resA = requests.post(url1, data=param_body1)  # request请求格式是url + json格式
                time.sleep(1)
                # resB = str(requests.post(url2, data=param_body).text)
                resB = requests.post(url2, data=param_body2)
                time.sleep(1)
                #print(json.loads(str(resB.text).replace("\n", ""), encoding='UTF-8'))
                if resA.status_code != 200 or resB.status_code != 200:
                    fw.write('{}\n{}\n{}\n'.format(counter, url1, resA.text))
                    fw.write('{}\n{}\n'.format(url2, resB.text))
                    fw.write('-' * 50)
            except:
                print("error, url is: " + "\n" + url1 + "\n")
                param_body1.pop('t_token')
                print(param_body1)
                pass

            counter += 1
            print(counter)

            dif = Diff()
            #print(resA.text)
            #print(resB.text)
            resA_json=json.loads(str(resA.text).replace("\n", ""), encoding='UTF-8')
            resB_json=json.loads(str(resB.text).replace("\n", ""), encoding='UTF-8')
            #print(resA_json)
            #print(resB_json)

            print(json.loads(str(resA.text).replace("\n", "")))
            print(json.loads(str(resB.text).replace("\n", "")))
            dif.diff(json.loads(str(resA.text).replace("\n", ""), encoding='UTF-8'),
                     json.loads(str(resB.text).replace("\n", ""), encoding='UTF-8'))
            # dif.diff(json.dumps(json.loads(resA.replace("\n", ""), encoding='UTF-8'),ensure_ascii=False),json.dumps(json.loads(resB.replace("\n", ""), encoding='UTF-8'),ensure_ascii=False))
            a = dif.result()  # diff 的结果
            print(a)

    except Exception as e:
        print(e)
    finally:
        f.close()
        fw.close()


if __name__ == '__main__':
    main(sys.argv)
