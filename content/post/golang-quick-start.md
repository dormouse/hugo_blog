---
title: "Golang Quick Start"
date: 2017-01-18 11:56:48
lastmod: 2017-01-18 11:56:48
tags: ["golang"]
categories: ["development"]
slug: "golang-quick-start"
description: "Golang by Google"
---



Quick Start
-----------

### ubuntu

Install golang:

    sudo apt-get install golang
    mkdir -p $HOME/go_work/src/github.com/username/hello
    export GOPATH=$HOME/work

For convenience, add the workspace's bin subdirectory to your .bashrc:

    export GOPATH=$HOME/go_work
    export PATH=$PATH:$GOPATH/bin

Save following to `$GOPATH/src/github.com/username/hello/hello.go`:

    package main

    import "fmt"

    func main() {
        fmt.Printf("hello, world\n")
    }

compile and run:

    go install github.com/username/hello
    $GOPATH/bin/hello

Done!

My first golang programe
------------------------

``` {.sourceCode .go}
package main

import "fmt"

// fibonacci
// fibonacci 函数会返回一个返回 int 的函数。
func fibonacci() func() int {
    count := 0
    a := 1
    b := 1
    return func() int {
        count++
        if count <= 2 {
            a = 1
            b = 1
            return 1
        }
        c := b
        b = a + b
        a = c
        return b
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
```

Study source
------------

-   [Golang tour (Simple Chinese)](https://tour.go-zh.org/list)
-   [Golang document](https://golang.org/doc/)

