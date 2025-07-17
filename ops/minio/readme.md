```sh
# https://min.io/docs/minio/linux/reference/minio-mc-admin/mc-admin-accesskey-list.html
# https://min.io/docs/minio/linux/integrations/aws-cli-with-minio.html

mc alias set myminio http://localhost:9000 minioadmin minioadmin
mc admin accesskey create myminio/
mc admin accesskey ls myminio
```
