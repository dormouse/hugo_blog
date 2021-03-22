---
title: "Install wordpress on LinuxMint(Ubuntu)"
date: 2014-10-26 19:45:34
tags: ["workpress","linuxmint"]
categories: ["linux"]
slug: "wordpress-on-linuxmint"
---

1.  install softwares:

    sudo apt-get install wordpress mysql-server phpmyadmin

2.  make links:

    sudo ln -s /usr/share/wordpress/ /var/www/wp
    sudo ln -s /usr/share/phpmyadmin/ /var/www/phpmyadmin

3.  restart services:

    sudo service apache2 restart
    sudo service mysql restart

4.  在phpmyadmin中创建wordpress专用用户
5.  config wordpress:

    cd /usr/share/wordpress
    mv wp-config.php wp-config.php.bak
    修改wp-config-sample.php 中的用户名和密码，另存为wp-config.php

6.  add administrator

open <http://127.0.0.1/wp/> ,set user name and password of wordpress's admin.
