---
layout: post
title: mysql_real_escape_string 正確的使用方式
date: 2014-05-12 04:29
comments: true
categories: 
---
[This thread][1]

``` php
<?php
	$string = iconv("UTF-8", "UTF-8//IGNORE", $string);
?>
```

[1]: http://stackoverflow.com/questions/5741187/sql-injection-that-gets-around-mysql-real-escape-string