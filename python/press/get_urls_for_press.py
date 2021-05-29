#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import getopt
import os
from log_filter import Log_filer
YF = 'xxxx'
ONLINE='xxxx'

def main(argv):
    helpStr = '{} -f <log_file_name> -v <app_version> -t <press_type> -H <host> -d <datatype> -c <convert_flag>'.format(argv[0])
    logFilter = Log_filer()
    log_file_name = 'log.txt'
    app_version = ''
    press_type = ''
    host = ''
    datatype=''

    try:
        opts, args = getopt.getopt(argv[1:], "hf:v:t:H:d:c:", ["logFileName=", "appVersion=", "type=", "host=","datatype=","convert_flag="])
    except getopt.GetoptError:
        print(helpStr)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(helpStr)
            sys.exit()
        elif opt in ("-f", "--logFileName"):
            log_file_name = arg
        elif opt in ("-v", "--appVersion"):
            app_version = arg
        elif opt in ("-t", "--type"):
            press_type = arg
        elif opt in ("-H", "--host"):
            host_type = arg
            if host_type == 'YF':
                host = YF
            elif host_type == 'OL':
                host = ONLINE
            else:
                print("Unsupport host type, only for YF or OL.")
                sys.exit(3)
        elif opt in("-d","--datatype"):
            data_type=arg
            if data_type=='realtime':
                datatype='realtime'
            elif data_type=='offline':
                datatype='offline'
            elif data_type=='all':
                datatype='all'
            else:
                print('unsupport datatype')
                sys.exit(3)
        elif opt in("-c","--convert_flag"):
            convert_flag=arg
        else:
            print('Unrecognized paramters')
            print(helpStr)
            sys.exit(3)
    print('appVersion='+app_version)
    logFilter.log_filer_for_press(log_file_name, app_version, press_type, host,datatype,convert_flag)


if __name__ == "__main__":
    main(sys.argv)
