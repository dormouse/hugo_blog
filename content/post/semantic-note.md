---
title: "Semantic Note"
date: 2017-05-11 10:43:00
lastmod: 2017-05-11 10:43:00
tags: ["semantic","note"]
categories: ["software"]
slug: "semantic-note"
description: "Note for Semantic."
---



Install
-------

Install NodeJs:

    brew install node

Install Gulp:

    npm install -g gulp

Install Semantic UI:

    npm install semantic-ui --save
    cd semantic/
    gulp build

Include in Your HTML:

    <link rel="stylesheet" type="text/css" href="semantic/dist/semantic.min.css">
    <script
      src="https://code.jquery.com/jquery-3.1.1.min.js"
      integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
      crossorigin="anonymous"></script>
    <script src="semantic/dist/semantic.min.js"></script>

Updating:

    npm update
