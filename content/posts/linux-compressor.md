---
title: "Linux 下压缩和解压缩"
date: 2014-10-20 14:42:05
categories: ["software"]
slug: "linux-compressor"
---



Linux下压缩文件种类繁多，这里简单介绍一下常用的命令。

常用压缩命令
------------

  扩展名             |解压                                          |打包
  ------------------ |--------------------------------------------- |-----------------------------------------------------------------
  .tar               |tar xvf FileName.tar                          |tar cvf FileName.tar DirName
  .tar.gz            |tar zxvf FileName.tar.gz                      |tar zcvf FileName.tar.gz DirName
  .tar.bz2           |tar jxvf FileName.tar.bz2                     |tar tar jcvf FileName.tar.bz2 DirName
  .gz                |gunzip FileName.gz gzip -d FileName.gz        |gzip FileName
  .bz2               |bzip2 -d FileName.bz2 bunzip2 FileName.bz2    |bzip2 -z FileName
  .bz                |bzip2 -d FileName.bz bunzip2 FileName.bz      |
  .tar.bz            |tar jxvf FileName.tar.bz                      |
  .Z                 |uncompress FileName.Z                         |compress FileName
  .tar.Z             |tar Zxvf FileName.tar.Z                       |tar Zcvf FileName.tar.Z DirName
  .tgz               |tar zxvf FileName.tgz                         |
  .tar.tgz           |tar zxvf FileName.tar.tgz                     |tar zcvf FileName.tar.tgz FileName
  .zip               |unzip FileName.zip                            |zip FileName.zip DirName
  .rar               |rar a FileName.rar                            |rar e FileName.rar
  .lha               |lha -e FileName.lha                           |lha -a FileName.lha FileName


.tar .tgz .tar.gz .tar.Z .tar.bz .tar.bz2 .zip

.cpio .rpm .deb .slp .arj .rar .ace .lha .lzh

.lzx .lzs .arc .sda .sfx .lnx .zoo .cab .kar .

cpt .pit .sit .sea

解压:

    sEx x FileName.*

压缩:

    sEx a FileName.* FileName

sEx只是调用相关程序，本身并无压缩、解压功能，请注意！

分卷压缩及解压分卷压缩文件
--------------------------

### 使用rar

1.分卷压缩

ubuntu下没有默认安装rar，可以通过 sudo apt-get install rar,sudo apt-get
install unrar 来安装rar.

安装过后，使用以下命令进行分卷压缩:

    rar a -vSIZE  压缩后的文件名 被压缩的文件或者文件夹

例如:

    rar a -v1024m foo.rar foo

此命令即为对foo文件夹进行分卷压缩，每卷的大小为1024m，压缩后的文件名为foo.rar

2.解压

对任何一个分卷执行:

    rar e foo.part1.rar

### 使用tar

1.分卷压缩:

    tar cvzpf - foo | split -d -b 50m

上面的命令是将foo这个文件夹分卷压缩，每卷50m，注意foo前面有空格.压缩完之后，会被命名为x00,x01,x02。。。

2.解压

首先需要合并：

合并的命令是:

    cat x*>foo.tar.gz

然后解压:

    tar xzvf foo.tar.gz
