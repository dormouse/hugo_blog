---
title: "Vim Note"
date: 2017-02-10
lastmod: 2017-02-16
tags: ["vim", "note"]
categories: ["software"]
slug: "vim-note"
---

Use MacVim in Command line
--------------------------

2017年 2月16日 星期四 22时46分40秒 CST

Add following in `./bash_profile`:

    alias gvim='/Applications/MacVim.app/Contents/MacOS/Vim -g'

Edit more than one file
-----------------------

### open file

#### Out vim

-   vim file1 file2 : open multiple files
-   vim -o file1 file2 : open multiple files with horizontal windows
-   vim -O file1 file2 : open multiple files with vertical windows

#### in vim

-

    e file

    :   open new file

-

    sp file

    :   open new file in hroizontal window

-

    vsp file

    :   open new file in vertical window

### close file

:bd close current buffer

:bd2 close buffer No.2

### switch file

:ls show files list

:n next file

:N previous file

Split Window
------------

-   `:sp` split horizontally
-   `:vs` split vertically

Shell
-----

date

-   `:shell`: open shell window. Use `exit` to quit shell window
-   `:!command`: run command in shell
-   `:r !command`: run command in shell, insert result to next line (ie:
    `:r !date`: insert date to nex line)

What is the &lt;Leader&gt; key?
-------------------------------

This section copy from:
http://stackoverflow.com/questions/1764263/what-is-the-leader-in-a-vimrc-file


The `<Leader>` key is mapped to `\` by default. So if you have a map of
`<Leader>t`, you can execute it by default with `\+t`. For more detail
or re-assigning it using the mapleader variable, see `:help leader`.

To define a mapping which uses the "mapleader" variable, the special
string "&lt;Leader&gt;" can be used.  It is replaced with the string
value of "mapleader". If "mapleader" is not set or empty, a backslash is
used instead.  

Example:

    :map <Leader>A  oanother line <Esc>

Works like:

    :map \A  oanother line <Esc>

But after:

    :let mapleader = ","

It works like:

    :map ,A  oanother line <Esc>

Note that the value of "mapleader" is used at the moment the mapping is
defined.  Changing "mapleader" after that has no effect for already
defined mappings.

Reference
---------

-   Vim Doc: <http://www.vim.org/docs.php>
-   Vim Cheat Sheet: <https://vim.rtorr.com/>

