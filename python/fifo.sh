date=`date +%Y-%m-%d -d '1 days ago'`
tmpfile=$$.fifo        #创建管道名称（就是个名字）  $$是进程号 
mkfifo $tmpfile       #创建管道 
exec 4<>$tmpfile   #创建文件标示4，以读写方式操作管道$tmpfile 
rm $tmpfile            #将创建的管道文件清除 
                                                                                 
thred=4                #指定并发个数 



#为并发线程创建相应个数的占位
{ 
for (( i = 1;i<=${thred};i++ ))  # 实现控制线程数
do 
echo;                  #因为read命令一次读取一行，一个echo默认输出一个换行符，所以为每个线程输出一个占位换行 从管道中读取行，每次读一行。每读一次就会减少一个空行，直到管道中没有回车符，所有行读取完毕后执行挂起，实现线程数量控制
done 
} >&4                  #将占位信息写入管道

CUR_PATH=`pwd`
SSHPASS="$CUR_PATH/tools/sshpass"
SSH="$SSHPASS -p $PASSWD ssh -o StrictHostKeyChecking=no -o GSSAPIAuthentication=no -n "

for ip in ${IPLIST}   #实现了一个并行读写 fifo管道实现多进程读写 
do
   read  # 每次读一行。每读一次就会减少一个空行，直到管道中没有回车符
  mkdir -p logs/${ip}
  $SSH admin@$ip "pwd" || true    #远程执行pwd
  $SSHPASS -p $PASSWD scp admin@${ip}:/export/Logs/ge/access/access.log  logs/${ip}/ || true   # 远程拉取日志
  echo >&4)& # &放后台执行 ， #任务在后台执行结束后，向文件描述符中写入一个空行。如果不在向描述符中写入空行，当后台放入THREAD_NUM个任务之后，由于描述符中没有可读取的空行，会导致read 停顿。
  done <&4 # 这里干什么？管道可以作为输入
  wait
exec 4>&- 关闭管道

cat logs/*/* >catalina.out 把获取的access.log都转成catalina.out
