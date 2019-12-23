docker rm -f uwsgi
docker run --name uwsgi \
--restart=always \
--dns=192.168.100.1 \
-e TZ='Asia/Shanghai' \
-p 8101:80 \
-d 192.168.100.71:5000/flk_monagent \
sh /uwsgi/startpython.sh

#-v /opt/python/uwsgi:/uwsgi \