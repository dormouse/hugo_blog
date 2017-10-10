---
title: "Sublime Text Note"
date: 2017-01-19 12:48:01
lastmod: 2017-09-25
tags: ["sublime","note"]
categories: ["software"]
slug: "sublime-text-note"
---

Install Sublime Text3
---------------------

### apt

Install the GPG key:

    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

Ensure apt is set up to work with https sources:

    sudo apt-get install apt-transport-https

Select the channel to use:

Stable:

    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

Dev:

    echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

Update apt sources and install Sublime Text:

    sudo apt-get update
    sudo apt-get install sublime-text

Install Package Control
-----------------------

Office Document: <https://packagecontrol.io/installation>

在 sublime text3 的终端中运行如下代码安装 Package Control
，终端打开方法为 使用 `ctrl +`\` 快捷键或者选择菜单
`View > Show Console` :

    import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

通过 `ctrl+shift+p` 进入 `Command Palette` ，输入
`Package Contorl: Install Package` (简写为 `ip` )，回车执行，
进入插件的搜索窗口，查找选择到需要的插件后，回车即可进行安装，
安装状态在最下面的状态栏内会有文字提示。

Install Packages
----------------

### Install Anaconda

Usage: <http://damnwidget.github.io/anaconda/IDE/>

Use Fcitx in Sublime Text 3
---------------------------

Sublime text 3 is not support fcitx, so patch it:

    $ wget https://github.com/yuan3y/sublime_zh_patch/archive/patch-1.zip
    $ unzip patch-1.zip
    $ cd sublime_zh_patch-patch-1/
    $ sudo ./setup.sh
    $ sudo apt-get install fcitx fcitx-config-gtk fcitx-googlepinyin fcitx-module-cloudpinyin fcitx-table-wubi

Play with evernote
------------------

Use Sublime Text plugin for Evernote, you and read and write evernote.

This package is based on SublimeEvernote for ST2 but is only supported
on ST3 and adds many new features.

To start using it install it from Package Control and type "Evernote" on
the Command Palette (`ctrl+shift+p`). See [First
Use](https://github.com/bordaigorl/sublime-evernote#first-use) for
linking the plugin to your account.

My Settings
-----------

Flowing is my settings:

    {
        "auto_complete": false,
        "color_scheme": "Packages/Color Scheme - Default/Monokai.tmTheme",
        "ensure_newline_at_eof_on_save": true,
        "file_exclude_patterns":[
            ".DS_Store",
            "*.pid",
            "*.pyc"
        ],
        "find_selected_text": true,
        "fold_buttons": false,
        "folder_exclude_patterns":[
            ".git",
            "__pycache__"
        ],
        "font_face": "ubuntu mono",
        // for OSX
        // "font_face": "PT Mono",
        "font_size": 12.0,
        "font_options":
        [
            "subpixel_antialias",
            "no_bold"
        ],
        "highlight_line": true,
        "ignored_packages": [],
        "line_padding_bottom": 1,
        "line_padding_top": 1,
        "rulers": [75, 80],
        "scroll_past_end": false,
        "show_full_path": true,
        "show_minimap": false,
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true
    }

Ref
---

-   <https://www.zhihu.com/question/33409254>
-   Sublime Text Document: [Linux Package Manager
    Repositories](https://www.sublimetext.com/docs/3/linux_repositories.html)

