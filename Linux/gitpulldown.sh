#!/bin/sh
source ~/.bash_profile  # 加上这个使别名生效

cd ~
# 判断文件夹是否存在，存在强制删除
if [ -d "downloaddir" ];then
rm -rf downloaddir
fi
mkdir downloaddir
cd ~/downloaddir
output=`git clone https://coding.jd.com/zhaocuixia/excise.git`
cd excise/app/src/main/res/layout

# 判断文件是否存在
if [ -f "activity_main.xml" ];then
echo '文件存在'
else
echo '文件不存在有问题'
exit 1
fi
# 定位进行首个匹配到的替换
sed -i  's/Hello World/Hello ZhaoCuiXia/' activity_main.xml
# 定位进行全部的替换
sed -i   's/Hello/Welcome/g' activity_main.xml
# 定位到某行,删除某行
sed -i  '/android:text/d' activity_main.xml
# 某行后进行添加
sed -i  '/android:layout_height/aandroid:text="new Hello world!"' activity_main.xml
git add .
git commit -m'对文件进行修改'
git push
