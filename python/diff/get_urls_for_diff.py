#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import getopt
import os
from log_filter import Log_filer

def main(argv):
    # helpStr = '{} -f <log_file_name> -v <app_version>'.format(argv[0])
    helpStr = '{} -f <log_file_name> '.format(argv[0])
    logFilter = Log_filer()
    log_file_name = 'log.txt'
    app_version = ''

    try:
        # opts, args = getopt.getopt(argv[1:], "hf:v:", ["logFileName", "appVersion="])
        opts, args = getopt.getopt(argv[1:], "hf:", ["logFileName"])
    except getopt.GetoptError:
        print(helpStr)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(helpStr)
            sys.exit()
        elif opt in ("-f", "--logFileName"):
            log_file_name = arg
        # elif opt in ("-v", "--appVersion"):
        #     app_version = arg
        else:
            print('Unrecognized paramters')
            print(helpStr)
            sys.exit(3)

    # print("app_version="+app_version)

    # logFilter.log_filter_for_diff(log_file_name, app_version)
    logFilter.log_filter_for_diff(log_file_name)



if __name__ == "__main__":
    main(sys.argv)
