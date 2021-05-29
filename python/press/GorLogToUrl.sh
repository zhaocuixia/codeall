ACCESS_KEY='xxx'
SECRET_KEY='xxx'
REGION='spark'
HOST_BUCKET='xx.xx.local'
HOST='xx.xx.local'
param="--access_key=$ACCESS_KEY --secret_key=$SECRET_KEY --region=$REGION --host-bucket=$HOST_BUCKET --host=$HOST --no-ssl"

tar -czvf app_urls_gor.tgz urls/app_urls_gor.gor
s3cmd put app_urls_gor.tgz s3://bpp_op_requests/bpp_quality/$JOB_NAME/app_urls/ $param

# 将生成的日志访问，上传到云

s3cmd signurl s3://bpp_op_requests/bpp_quality/$JOB_NAME/app_urls/app_urls_gor.tgz 60480000000 $param >app_urls_gor.url

# 并提供一个url进行访问，其设置了有效期，并将URL保存在app_urls_gor.url文件中
