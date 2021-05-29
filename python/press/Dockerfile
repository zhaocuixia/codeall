ENV LANG zh_CN.UTF-8
RUN yum install -y  wget iptraf lrzsz which net-tools lsof psmisc lftp libpcap libpcap-devel nscd
RUN mkdir -p /home/export/servers && wget -q -t 2 ftp://mfs.jd.com:/mnt/mfs/jenkins/jobs/goreplay/lastSuccessful/archive/src/github.com/buger/goreplay/goreplay -O /home/export/servers/gor && chmod +x /home/export/servers/gor
ADD press/jdos/docker_start.sh  /home/admin
ENTRYPOINT sh /home/admin/docker_start.sh && sleep 9999999d
