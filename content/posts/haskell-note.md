---
title: "Haskell 笔记"
date: 2015-05-18
lastmod: 2015-05-18
tags: ["haskell","note"]
categories: ["haskell"]
slug: "haskell-note"
---



入门
----

安装:

    sudo apt-get install ghc

终端命令:

    ghci

可以用ghci的 :set prompt 来进行修改:

    Prelude> :set prompt "ghci>"
    ghci>

导入模块:

    ghci> :module + Data.Ratio

我们探索类型世界的第一步是修改
ghci，让它在返回表达式的求值结果时，打印出这个结果的类型。使用 ghci 的
:set命令可以做到:

    Prelude> :set +t

取消:

    Prelude Data.Ratio> :unset +t

列表
----

加:

    Prelude> [1,2] ++ [3,4]
    [1,2,3,4]

第一个:

    Prelude> head [1, 2, 3, 4]
    1

除第一个以外:

    Prelude> tail [1, 2, 3, 4]
    [2,3,4]

前 N 个:

    Prelude> take 2 [1, 2, 3, 4, 5]
    [1,2]

前 N 个以外:

    Prelude> drop 2 [1, 2, 3, 4, 5]
    [3,4,5]

嵌套使用:

    Prelude> head (drop 2 "azety")
    'e'

元组
----

二元元组取值:

    Prelude> fst (1, 'a')
    1
    Prelude> snd (1, 'a')
    'a'
