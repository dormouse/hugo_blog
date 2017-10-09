---
title: "Git Note"
date: 2017-02-11
lastmod: 2017-02-11
tags: ["git","note"]
categories: ["software"]
slug: "git-note"
description: "Note for git."
---



Basic Usage
-----------

添加文件:

    git add README test.rb LICENSE

提交变动:

    git commit -m 'initial commit of my project'
    git commit -a -m 'made a change'

列出当前所有分支,前面带星号的是当前所有分支:

    git branch

查看各个分支最后一个提交对象的信息:

    git branch -v：

创建分支:

    git branch test

切换分支:

    git checkout test

创建并切换到新分支:

    git checkout -b iss53

合并分支，下例把 hotfix 分支并入 master 分支:

    git checkout master
    git merge hotfix

删除分支:

    git branch -d hotfix

查询合并时产生的冲突:

    git status

可视化的解决冲突的工具:

    git mergetool

要从该清单中筛选出你已经（或尚未）与当前分支合并的分支， 可以用 --merge
和 --no-merged 选项（Git 1.5.6 以上版本）。 比如用git branch --merge
查看哪些分支已被并入当前分支， 也就是说哪些分支是当前分支的直接上游:

    git branch --merged
      iss53
    * master

另外可以用 git branch --no-merged 查看尚未合并的工作:

    git branch --no-merged
        testing

.gitignore 不起作用:

    git rm -r --cached _build/*

### submodule

增加 submodule:

    git submodule add https://github.com/klen/python-mode.git bundle/ropevim

删除 submodule:

    git rm --cache bundle/pep8
    rm -rf bundle/pep8
    del contene in .gitmodules

### 用命令行创建新的 repository

Craet new repo:

    echo "# vim-python-ide" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin git@github.com:dormouse/vim-python-ide.git
    git push -u origin master

Use existing repo:

    cd existing_git_repo
    git remote add origin https://git.oschina.net/mouselinux/test.git
    git push -u origin master

使用 Github
-----------

### 设置 Git

设置用户名和电子邮件:

    git config --global user.name "Your Name Here"
    git config --global user.email "your_email@example.com"

### 生成 SSH 密钥

第一步：检查 \~/.ssh 下有无 id\_rsa.pub 或 id\_dsa.pub
文件，如果两个都没有，那么 可以开始第二步，否则直接跳到第3步。

第二步：生成新的 SSH 密钥

生成密钥可以使用如下命令。程序会询问密钥储存的位置，如果使用缺省位置则直接按
回车即可:

    ssh-keygen -t rsa -C "your_email@example.com"
    # Creates a new ssh key, using the provided email as a label
    # Generating public/private rsa key pair.
    # Enter file in which to save the key (/home/you/.ssh/id_rsa):

    Now you need to enter a passphrase.
    Why do passphrases matter?

    # Enter passphrase (empty for no passphrase): [Type a passphrase]
    # Enter same passphrase again: [Type passphrase again]

    Which should give you something like this:

    # Your identification has been saved in /home/you/.ssh/id_rsa.
    # Your public key has been saved in /home/you/.ssh/id_rsa.pub.
    # The key fingerprint is:
    # 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your_email@example.com

第三步：把 SSH 密钥添加到 GitHub

把 id\_rsa.pub 的内容添加到 GitHub:

    cat ~/.ssh/id_rsa.pub

第四步：测试密钥是否添加成功

使用如下命令:

    ssh -T git@github.com
    # Attempts to ssh to github

可能会看到如下出错信息:

    ...
    Agent admitted failure to sign using the key.
    debug1: No more authentication methods to try.
    Permission denied (publickey).

在某些 Linux 发行版中会出现这个问题，正常的。

可以会看到如下警告:

    # The authenticity of host 'github.com (207.97.227.239)' can't be established.
    # RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
    # Are you sure you want to continue connecting (yes/no)?

这也是正常的，写上“ yes ”就可以了，然后就会看到:

    # Hi username! You've successfully authenticated, but GitHub does not
    # provide shell access.

如果 username 是正确的名字，那就成功了。

如果看到“ access denied ”的字样，那么就只能使用 HTTPS 方法吧。

How to resolve the conflict
---------------------------

### Let's make a test

Clone same git to different folder:

    $ git clone https://your-git test1
    $ git clone https://your-git test2

There is a `test.txt` file which have following lines in git:

    Line1:11111
    Line2:22222
    Line3:33333
    Line4:44444

Change `test2/test.txt` file to following lines, commit and push it:

    Line1:11111
    Line2:22222AA
    Line3:33333
    Line4:44444

Change `test1/test.txt` file to following lines, commit and push it:

    Line1:11111
    Line2:22222
    Line3:33333BB
    Line4:44444

Now the remote server will refuse the push, so we have to pull first.
And Now `test1/test.txt` will change to following lines:

    Line1:11111
    <<<<<<< HEAD
    Line2:22222
    Line3:33333BB
    =======
    Line2:22222AA
    Line3:33333
    >>>>>>> 763db9d983ae8dec88417684eeab6198af9d4e27
    Line4:44444

Content between `<<<<<<< HEAD` and `=======` is your local change,
Content between `=======` and `>>>>>>> 763db...` is remote change. So
just edit `test1/test.txt` , commit and push it.
