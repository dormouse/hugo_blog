---
title: "github.io 丢失下划线开头的文件"
date: 2014-10-18 21:58:29
tags: ["github","jekyll"]
categories: ["linux"]
slug: "files-that-start-with-an-underscore-are-missing"
---



近来开始在 github.io 上写 blog ,但是发现 github 不支持下划线开头的目录。
于是写 Email 向 github 求助，很快就得到回复。原来是 Jekyll （亦或是
ruby?) 的 问题。 Jekyll 不支持点号、井号或下划线开头的东东。

-   解决方法：

> 在根目录加入一个 .nojekyll 文件，来关闭 Jekyll 。

-   参考：

> [files-that-start-with-an-underscore-are-missing](https://help.github.com/articles/files-that-start-with-an-underscore-are-missing/)
