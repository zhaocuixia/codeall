#!/usr/bin/python
#-*-coding:UTF-8-*-

from scapy.all import *
import time,os,sys
import multiprocessing

#抓包并存入pcap文件
def capture_pcap(host,face,num,pcap_path):
    IP='ip dst %s and tcp'%host
    package = sniff(iface=face, filter=IP, count=num)
    print(package)
    if os.path.exists(pcap_path):
        os.remove(pcap_path)
        time.sleep(1)
    wrpcap(pcap_path, package)

#解包
def unpackage(pcap_file):
    packets = rdpcap(pcap_file)
    for data in packets:
        if 'TCP' in data and 'Raw' in data:
           #s = repr(data)
            # print(data.getlayer('Raw').fields['load'])
            c = data.getlayer('Raw').fields['load'].decode('utf-8',errors='ignore').strip()
            if c.startswith('GET') and 'ajax?'in c:
                t = c.find('&uuid')
                if t<0:
                    t=c.find('uuid')
                print(c[4:t])

#抓包回调函数，将ajax数据写入文件
def packet_callback(packet,file_path,filter_str=''):
    data=str(packet[0]['TCP'])
    flag=False
    if filter_str=='' or filter_str==None:
        if 'ajax?' in data:
            flag=True
            t = data.find('GET')
            end = data.find('&uuid')
            if end < 0:
                end = data.find('uuid')
            print(data[t + 4:end])
    else:
        if 'ajax?' in data and filter_str not in data:
            flag=True
            t = data.find('GET')
            end = data.find('&uuid')
            if end < 0:
                end = data.find('uuid')
            print(data[t + 4:end])
    # 如果文件存在则后续追加写入，如果不存在创建新文件并写入
    if flag:
        if os.path.exists(file_path):
            f = open(file_path, 'at')
            f.write(data[t + 4:end] + '\n')
            f.close()
        else:
            f = open(file_path, 'wt+')
            f.write(data[t + 4:end] + '\n')
            f.close()

#抓取指定域名下的数据包,并调用回调函数处理
def capture_callback(host,face,fun,filter_string):
    path = os.getcwd()
    file_name=host+'.txt'
    file_path=path+os.sep+file_name
    if os.path.exists(file_path):
        os.remove(file_path)
    IP = 'ip dst %s' % host
    print(IP)
    package = sniff(iface=face, filter=IP,prn=lambda x: fun(x, file_path,filter_str=filter_string))

if __name__=='__main__':
    # array=sys.argv
    # hosts=array[1]
    #filter_string=array[2]
    # timeout = array[3]
    #num=array[4]
    #hosts =['ppzh.jd.com','ppzh.bdp.jd.com']
    hosts='ppzh.jd.com'
    face = 'Intel(R) Dual Band Wireless-AC 8265'
    timeout = 60
    #filter_string='getWatermark'
    filter_string=''
    num = 400
    pcap_path=r'D:\python_code\capture\test.pcap'
    # capture_pcap(host1,face,num,pcap_path)
    # time.sleep(2)
    # unpackage(pcap_path)

    #开启两个进程分别抓取不同域名下的ajax
    # for host in hosts:
    #     p=multiprocessing.Process(target=capture_callback,args=(host,face,packet_callback))
    #     #p.daemon=True
    #     p.start()
    #     #p.join()
    if isinstance(hosts,str) or (isinstance(hosts,list) and len(hosts)==1):
        capture_callback(hosts, face, packet_callback, filter_string)
    if isinstance(hosts,list) and len(hosts)>1:
        num1 = len(hosts)
        pool = multiprocessing.Pool(processes=num1)
        for host in hosts:
            pool.apply_async(capture_callback, (host, face, packet_callback, filter_string))
        pool.close()
        pool.join()










