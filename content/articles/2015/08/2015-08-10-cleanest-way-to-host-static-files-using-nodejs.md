---
layout: post
title: Cleanest way to host static files using nodejs
date: 2015-08-10 16:35
comments: true
categories:
---
Use built-in `http` module and `ecstatic` for middleware.

First, install ecstatic

``` sh
npm install ecstatic
```

And the magic!

``` js
var http = require('http'),
    ecstatic = require('ecstatic');

http.createServer(ecstatic({root:'./'}))
    .listen(8080, '127.0.0.1');
```
