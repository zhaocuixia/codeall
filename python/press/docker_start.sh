#!/bin/bash
VOCAB_NAME=$VOCAB_NAME
DOMAIN=$DOMAIN 
HOST=$HOST
EXTEND_PARAM=$EXTEND_PARAM
BASE_QPS=$BASE_QPS
URL=$URL
init_env(){
    rm -rf /export/servers && mv /home/export/servers /export
    ln -sf /export/servers /home/export/servers
    useradd admin
    chown admin:admin $0
    chown admin:admin /export/servers -R
    for item in `cat /proc/1/environ |tr '\0' '\n'`
    do
       echo $item >> /home/admin/.bashrc
    done
    sed  -i '/^HOME=/d'  /home/admin/.bashrc
    source /home/admin/tags
    export LANG=zh_CN.UTF-8
    sed -i 's/positive-time-to-live.*hosts.*\(.*\)[0-9]\(.*\)/\1positive-time-to-live\thosts\t\t3600\2/' /etc/nscd.conf 
    sed -i 's/negative-time-to-live.*hosts.*\(.*\)[0-9]\(.*\)/\1negative-time-to-live\thosts\t\t2\2/' /etc/nscd.conf
    /usr/sbin/nscd
    /usr/sbin/sshd
    /usr/sbin/crond
    echo "$_ROOT_"|passwd --stdin root
    echo "$_ADMIN_"|passwd --stdin admin
}
source /home/admin/.bashrc
[[ ! -L /home/export/servers ]] && init_env
cat > /home/admin/start.sh << EOF
#!/bin/bash
source /home/admin/.bashrc
source /home/admin/tags

wget -q -t 3 -w 2 "$URL" -O /export/servers/request.tgz
tar -vxf /export/servers/request.tgz 
mv urls/app_urls_gor.gor /export/servers/request.gor
timeout 3h /export/servers/gor --input-file "/export/servers/request.gor" --output-http "$HOST" --output-http-timeout 15s --input-file-loop --output-qps $BASE_QPS $EXTEND_PARAM &>> /export/error.log
exit 0
EOF
cat > /home/admin/stop.sh << EOF
#!/bin/bash
killall gor
pro_num=\`ps -ef|grep gor |grep -v grep|wc -l\`
[[ \$pro_num -ne 0 ]] && echo "stop failed" && exit 1
echo "stop success"
exit 0
EOF
chmod +x /home/admin/stop.sh /home/admin/start.sh
sh /home/admin/start.sh > /dev/null 2>&1
exit 0
