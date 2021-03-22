---
title: "Vim As IDE"
date: 2017-02-08 18:57:00
lastmod: 2017-02-08 18:57:00
tags: ["vim"]
categories: ["software"]
slug: "vim-as-ide"
---

Install Vundle
--------------

Vundle is short for Vim bundle and is a Vim plugin manager.

Official site: <https://github.com/VundleVim/Vundle.vim>

Use following command to install Vundle:

    $ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

Put following lines at the top of your .vimrc to use Vundle. Remove
plugins you don't need, they are for illustration purposes:

    set nocompatible              " be iMproved, required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'

    " The following are examples of different formats supported.
    " Keep Plugin commands between vundle#begin/end.
    " plugin on GitHub repo
    Plugin 'tpope/vim-fugitive'
    " plugin from http://vim-scripts.org/vim/scripts.html
    Plugin 'L9'
    " Git plugin not hosted on GitHub
    Plugin 'git://git.wincent.com/command-t.git'
    " git repos on your local machine (i.e. when working on your own plugin)
    Plugin 'file:///home/gmarik/path/to/plugin'
    " The sparkup vim script is in a subdirectory of this repo called vim.
    " Pass the path to set the runtimepath properly.
    Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
    " Install L9 and avoid a Naming conflict if you've already installed a
    " different version somewhere else.
    Plugin 'ascenator/L9', {'name': 'newL9'}

    " All of your Plugins must be added before the following line
    call vundle#end()            " required
    filetype plugin indent on    " required
    " To ignore plugin indent changes, instead use:
    "filetype plugin on
    "
    " Brief help
    " :PluginList       - lists configured plugins
    " :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
    " :PluginSearch foo - searches for foo; append `!` to refresh local cache
    " :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
    "
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line

Two ways to Install Plugins
---------------------------

-   Launch `vim` and run `:PluginInstall`
-   To install from command line: `vim +PluginInstall +qall`

My .vimrc
---------

2014年 10月 20日 星期一 20:24:31 CST

There is my .vimrc:

    set nocompatible              " be iMproved, required
    filetype off                  " required

    " set the runtime path to include Vundle and initialize
    set rtp+=~/.vim/bundle/Vundle.vim
    call vundle#begin()
    " alternatively, pass a path where Vundle should install plugins
    "call vundle#begin('~/some/path/here')

    " let Vundle manage Vundle, required
    Plugin 'VundleVim/Vundle.vim'

    " The following are examples of different formats supported.
    " Keep Plugin commands between vundle#begin/end.

    " plugin on GitHub repo
    Plugin 'vim-scripts/VimIM'
    " for file tree list
    Plugin 'scrooloose/nerdtree'
    Plugin 'scrooloose/nerdcommenter'

    " plugin from http://vim-scripts.org/vim/scripts.html
    " Plugin 'L9'

    " Git plugin not hosted on GitHub
    " Plugin 'git://git.wincent.com/command-t.git'

    " git repos on your local machine (i.e. when working on your own plugin)
    " Plugin 'file:///home/gmarik/path/to/plugin'

    " The sparkup vim script is in a subdirectory of this repo called vim.
    " Pass the path to set the runtimepath properly.
    " Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
    " Install L9 and avoid a Naming conflict if you've already installed a
    " different version somewhere else.
    " Plugin 'ascenator/L9', {'name': 'newL9'}

    " All of your Plugins must be added before the following line

    call vundle#end()            " required
    filetype plugin indent on    " required
    " To ignore plugin indent changes, instead use:
    " filetype plugin on
    "
    " Brief help
    " :PluginList       - lists configured plugins
    " :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
    " :PluginSearch foo - searches for foo; append `!` to refresh local cache
    " :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
    "
    " see :h vundle for more details or wiki for FAQ
    " Put your non-Plugin stuff after this line


    set autoindent
    set columns=85
    set expandtab
    set ignorecase
    set shiftwidth=4
    set tabstop=4
    set lines=40
    set number
    set nobackup


    "解决中文字符显示半个的问题
    set ambiwidth=double

    """""""""""""""""""""""""""""
    "解决windows下的中文乱码问题
    """""""""""""""""""""""""""""
    set encoding=utf-8
    "set termencoding=utf-8
    set fileencodings=ucs-bom,utf-8,chinese,latin-1
    if has("win32")
        set fileencoding=chinese
        "解决中文菜单乱码
        set langmenu=zh_CN.utf-8
        source $VIMRUNTIME/delmenu.vim
        source $VIMRUNTIME/menu.vim
        "解决console输出乱码
        language messages zh_cn.utf-8
        "设置字体
        "取得当前使用的字体：set guifont?
        "如果字体名称中含有空格，需要在空格前面加上一个反斜杠(\)：
        "set guifont=Terminal:h18:b:cANSI
        set guifont=Fixedsys
    else
        set fileencoding=utf-8
        set guifont=文泉驿等宽微米黑\ 12
    endif

    """""""""""""""""""""""
    " 设定 vimdiff 的颜色 "
    """""""""""""""""""""""
    if &diff
        set tw=80 columns=180
        " 设定超过的部份会自动换行，适合搭配显示行号使用
        " Add 代表新增的一行， Delete 代表删除的一行，
        " Change 代表有差异的一行，Text 代表有差异的这一行中，具有差异的部份
        hi DiffAdd ctermfg=Grey ctermbg=Blue guifg=Black guibg=LightBlue
        hi DiffDelete ctermfg=Grey ctermbg=Grey guifg=Grey
        hi DiffChange ctermfg=Black ctermbg=DarkGreen guifg=Black guibg=LightGray
        hi DiffText ctermfg=Black ctermbg=Grey guifg=Black guibg=Gray
    endif

    """""""""""
    " 设定TAG "
    """""""""""
    set foldmethod=syntax " 用语法高亮来定义折叠
    set foldmethod=indent " 更多的缩进表示更高级别的折叠(这个似乎效果好一些)
    let Tlist_Show_One_File = 1 "不同时显示多个文件的tag，只显示当前文件的。
    let Tlist_Exit_OnlyWindow = 1 "如果 taglist 窗口是最后一个窗口，则退出 vim。
    let Tlist_Auto_Open=1 "自动打开Tlist
    "let Tlist_Use_Right_Window = 1 "在右侧窗口中显示 taglist 窗口。

    map <F5> :!python %<CR>
    map <F8> :w<CR>:!python3 %<CR>
    colorscheme slate
