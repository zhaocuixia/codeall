#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import sys
import getopt


def main(argv):
    #YF_URL = 'http://xxxx.php??'
    #ONLINE_URL = 'http://xxxx.php?'
    TOKEN = 'tester:xxxx'
    filepath = 'app_urls_diff.txt'
    fullpath = sys.path[0] + os.sep + 'urls' + os.sep + filepath
    resultFile = 'log2postman.log'
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
        f = open('/Users/zhaocuixia/app_urls_diff.txt')
        counter = 0
        while True:
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

            param1 = json.dumps(param_body1)
            param1 = param1.replace('\": \"', '=')
            param1 = param1.replace('\", \"', '&')
            url1 = url1 + '&' + param1[2:-2]

            param2 = json.dumps(param_body2)
            param2 = param2.replace('\": \"', '=')
            param2 = param2.replace('\", \"', '&')
            url2 = url2 + '&' + param2[2:-2]
            fw.write('-' * 50)
            counter += 1
            fw.write('{}\n'.format(counter))
            fw.write('{}\n{}'.format('线上url', url1))
            fw.write('{}\n'.format(''))
            fw.write('{}\n{}'.format('测试url',url2))
            fw.write('{}\n'.format(''))

    except Exception as e:
        print(e)
    finally:
        f.close()
        fw.close()


if __name__ == '__main__':
    main(sys.argv)


