# meiduo_project
腕表商城基于美多商城环境开发，前端采用Vue+Html+Css+JavaScript,后端采用django框架。
前台采用前后端不分离的开发模式，后台采用前后端分离的开发模式
## 项目启动过程
**启动redis** 

```redis-server --protected-mode no /etc/redis/redis.conf```

**启动FastDFS**

```sudo docker run -dti --rm --network=host --name tracker -v /var/fdfs/tracker:/var/fdfs delron/fastdfs tracker```

```sudo docker run -dti --rm --network=host --name storage -e TRACKER_SERVER=192.168.247.135:22122 -v /var/fdfs/storage:/var/fdfs delron/fastdfs storage```


**启动Elasticsearch**

```sudo docker run -dti --rm --name=elasticsearch --network=host -v /home/python/elasticsearch-2.4.6/config:/usr/share/elasticsearch/config delron/elasticsearch-ik:2.4.6-1.0```

**启动celery**

```celery -A celerytasks.main worker -l info```

**前台运行 端口号:8000** 

```npm install```

```npm run dev```

**后台运行 端口号:8000**

```python manage.py runserver```
