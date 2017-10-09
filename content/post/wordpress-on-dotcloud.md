---
title: "dotcloud 部署 wordpress"
date: 2012-01-06
tags: ["workpress","dotcloud"]
categories: ["linux"]
slug: "wordpress-on-dotcloud"
---



安装环境并创建项目
------------------

首先在 dotcloud 网站注册，并记录 api key 。

安装 dotcloud 环境:

    $ sudo easy_install dotcloud

运行以下命令，根据提示输入 api key:

    $ dotcloud

创建项目:

    $ mkdir wordpress
    $ cd wordpress
    $ dotcloud create dormouse

创建以下内容的dotcloud.yml:

    www:
      type: php
    db:
      type: mysql

推送项目:

    dotcloud push dormouse

查看项目信息
------------

全站信息:

    $ dotcloud info dormouse

显示以下内容:

    db:
        config:
            mysql_masterslave: true
            mysql_password: Y2##########CfUl89
        instances: 1
        type: mysql
    www:
        config:
            phpfpm_processes: 4
            static: static
        instances: 1
        type: php
        url: http://dormouse-dormouse.dotcloud.com/

www 信息:

    $ dotcloud info dormouse.www

显示以下内容:

    aliases:
    - dormouse-dormouse.dotcloud.com
    build_revision: rsync-1324737409417
    config:
        phpfpm_processes: 4
        static: static
    created_at: 1324737411.1332741
    datacenter: Amazon-us-east-1b
    image_version: e48799ec7395 (latest)
    ports:
    -   name: ssh
        url: ssh://dotcloud@dormouse-dormouse.dotcloud.com:20266
    -   name: http
        url: http://dormouse-dormouse.dotcloud.com/
    state: running
    type: php

数据库信息:

    $ dotcloud info dormouse.db

显示以下内容:

    config:
        mysql_masterslave: true
        mysql_password: Y2We#######33###
    created_at: 1324737411.5351181
    datacenter: Amazon-us-east-1a
    image_version: 1120eda9aa82 (latest)
    instances:
        dormouse.db.0:
            role: master
            state: up
    ports:
    -   name: ssh
        url: ssh://mysql@dormouse-dormouse.dotcloud.com:20270
    -   name: mysql
        url: mysql://root:Y2Wev5piHNyXs3CfUl89@dormouse-dormouse.dotcloud.com:20269
    type: mysql

数据库管理
----------

远程管理数据库，添加用户:

    $ dotcloud run dormouse.db -- mysql -u root -Y2We#######33###  //登录
    mysql>CREATE USER 'wp' IDENTIFIED BY '98####'; //创建用户“wp”，密码为98####
    mysql>CREATE DATABASE wp;  //创建数据库 wp
    mysql>GRANT ALL ON wp.* TO 'wp'@'%'; //赋予 wp 用户拥有 wp 数据库的所有权限
    mysql>FLUSH PRIVILEGES; //刷新使生效

    mysql>wp < mydb.sql //导入数据
    mysql>drop database wp //删除 wp 数据库

下载安装wordpress
-----------------

ssh 登录后操作:

    $ dotcloud ssh quany.www
    $ cd current
    $ wget http://wordpress.org/latest.tar.gz
    $ tar  zxvf latest.tar.gz
    $ cd wordpress
    $ cp -r ** ../
    $ cd ../
    $ rm -rf ** wordpress

因为解压出来的是一个文件夹，所以上面4个命令是把文件夹的文件全部复制到根目录下并删除原来的文件夹。

另：https://api.wordpress.org/secret-key/1.1/salt/

重写URL
-------

wordpress在Dotcloud的服务器Nginx的URL重写规则，新建nginx.conf并输入以下内容:

    try_files $uri $uri/ /index.php;

上传文件并重启服务器:

    $ dotcloud ssh quany.www              //登录SSH
    $ scp nginx.conf quany.www:~/current/nginx.conf   //用SCP安全上传
    $ supervisorctl restart php5-fpm     //重启php5-fpm进程
    $ sudo /etc/init.d/nginx restart     //重启nginx进程

强制https访问
-------------

在nginx.conf中加入以下内容:

    if ($http_x_forwarded_port != 443) { rewrite ^ https://$http_host/; }

绑定域名
--------

创建一条域名的CNAME记录到gateway.dotcloud.com就可以访问了:

    $ dotcloud alias add quany.www www.quany.info

删除应用和服务
--------------

删除应用:

    $ dotcloud destroy quany

删除服务:

    $ dotcloud destroy quany.www

使用ssh shell
-------------

使用命令:

    ~/bin/dotCloud ssh wiwi.www

或者:

    ~/bin/dotCloud info wiwi.www

之后，看端口号。

用 \~/.dotcloud/dotcloud.key 登录进去,在 .ssh 目录下建立一个
config文件，内容 如下:

    Host wiwi.www
    HostName wiwi-wikimiao.dotcloud.com
    Port 1234
    User dotcloud
    IdentityFile ~/.dotcloud/dotcloud.key

然后执行:

    ssh -v wiwi.www
    ssh -N -v wiwi.www -D 127.0.0.1:7070
