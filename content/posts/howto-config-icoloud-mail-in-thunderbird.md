---
title: "How to configure iCloud mail in Mozilla Thunderbird"
date: 2017-01-25
tags: ["mail","thunderbird"]
categories: ["software"]
slug: "howto-config-icoloud-mail-in-thunderbird"
description: "How to configure iCloud mail in Mozilla Thunderbird"
---



Incoming:

    Protocol: IMAP
    Server: imap.mail.me.com
    Port: 993
    SSL: SSL/TLS
    Authentication: Normal password

Outgoing:

    Protocol: SMTP
    Server: smtp.mail.me.com
    Port: 587
    SSL: STARTTLS
    Authentication: Normal password

Username for both should just be your actual username "dormouse.young",
not your whole email address.
