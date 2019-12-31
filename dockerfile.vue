FROM node:8-alpine3.9
RUN echo  'http://mirrors.ustc.edu.cn/alpine/v3.9/main'> /etc/apk/repositories && \
    echo  'http://mirrors.ustc.edu.cn/alpine/v3.9/community' >>/etc/apk/repositories && \
    cat /etc/apk/repositories
RUN apk add  --no-cache git python python2 && \
   git clone https://github.com/PanJiaChen/vue-element-admin.git 
RUN apk add make && \
   cd vue-element-admin && \
   npm install --registry=https://registry.npm.taobao.org
WORKDIR vue-element-admin
CMD [ '/usr/bin/npm','run','dev' ]  
