#!/bin/sh
source ~/.bash_profile  # 加上这个使别名生效mac下载了gsed,设置了gsed的别名为sed
# 判断文件是否存在
cd ~
if [ -f "test.log" ];then
echo '文件存在'
else
echo '文件不存在有问题'
exit 1
fi

# 替换
sed -i  's/SPUtil.getERP()/zhaocuixia/' test.log
sed -i  's/SPUtil.getToken()/zhaocuixia333/' test.log

# 删除匹配行的下行
sed -i '/PasswordVerifyActivity.class/{n;d}' test.log
# 删除匹配行的上行
sed -i  '$!N;/\n.*PasswordVerifyActivity.class/!P;D' test.log
# 删除匹配行及下行
sed -i  '/LoginActivity.class/,+1d' test.log
# 添加
sed -i  "/initClick()/averifySuccess();" test.log
