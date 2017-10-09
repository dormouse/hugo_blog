---
title: "Linux Mint 17 安装笔记"
date: 2014-10-16 20:31:00
tags: ["linuxmint"]
categories: ["linux"]
slug: "install-linuxmint17"
---



Install cloudstation
--------------------

-   Download cloudstation
-   Uncompress
-   ./install

Select software source
----------------------

Select the fastest software source

Install some software
---------------------

-   Install following software:

        sudo apt-get install build-essential python-dev
        sudo apt-get install fcitx fcitx-ui-classic fcitx-table-wbpy
        sudo apt-get install git vim-gnome ctags keepassx filezilla

-   Software setup

    > -   Sync firefox
    > -   Setup git, see : [Github
    >     Setup](%7Bfilename%7Dgithub-setup.rst)

Install virtualenv
------------------

-   Install pip and virtualenvwrapper:

        sudo apt-get install python-pip
        sudo pip install virtualenvwrapper

-   Add flowing to \~/.bashrc:

        export WORKON_HOME=$HOME/.virtualenvs
        export PROJECT_HOME=$HOME/project
        source /usr/local/bin/virtualenvwrapper.sh
        reload .bashrc

Install XBMC
------------

输入如下命令安装（适用于 Ubuntu 9.10 Karmic 或更高版本，详见：
[Install\_XBMC\_on\_Ubuntu/HOW-TO](http://wiki.xbmc.org/index.php?title=HOW-TO:Install_XBMC_on_Ubuntu/HOW-TO_1)
）:

    sudo apt-get install python-software-properties pkg-config
    sudo add-apt-repository ppa:team-xbmc
    sudo apt-get update
    sudo apt-get install xbmc xbmc-standalone

安装完以后要设置字体：进入 XBMC，菜单 System -&gt; Appearance -&gt; Skin
-&gt; Fonts -&gt; 选择 Arial based 。
