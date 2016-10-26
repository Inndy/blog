---
layout: post
title: SQL Injection 是怎麼發生的
date: 2015-03-29 06:10
comments: true
categories: 
---
# SQL Injection 是怎麼發生的？

這篇文章原本是要寫給學校的老師看的，覺得可以拿來資安科普所以就貼到 Blog 吧！

首先，考慮以下 PHP 程式碼

``` php
<?php
function login($user, $pass) {
	$sql = "SELECT * FROM `users` WHERE `name` = '$user' AND `password` = SHA1('$pass')";
	$user = query($sql);
	if (count($user) > 0)
	    return $user[0];
	else
	    return false;
}

$user = login($_POST['user'], $_POST['pass']);
if ($user !== false)
    echo "登入成功：" . $user['name'];
else
    echo "登入失敗！";
```

使用者輸入資料：

`user=%27%20or%20%27%27%20%3D%20%27%27%20--&pass=aaaaaaa`

解碼後（`--` 和 `#` 是 SQL 註解）

`user` -> `' or '' = '' --` , `pass` -> `aaaaaaa`

進入 PHP 組合成 SQL 語句

``` sql
SELECT * FROM `users` WHERE `name` = '$user' AND `password` = SHA1('$pass')
```

帶入資料後

``` sql
SELECT * FROM `users` WHERE `name` = '' or '' = '' --' AND `password` = SHA1('aaaaaaa')
```

由於 `' or '' = '' --` 造成一個永遠成立 (`某些條件 or True`)，就可以繞過驗證登入

另外一些技巧，如：

``` sql
SELECT * FROM `topics` WHERE `id` = '$id'
```

帶入

`$id` = `-1' UNION SELECT * FROM users --`

組合後

``` sql
SELECT * FROM `topics` WHERE `id` = '-1' UNION SELECT * FROM users --'
```

會造成 `id = -1` 不存在，select不出任何東西，但是 union select 會撈出別的資料


除此之外，就算是 `checkbox`, `select`, `radio` 都有可能修改其 value，所以只要是從 user 出來的資料，一律要經過過濾

推薦閱讀文章：[如何正確的取得使用者 IP？ (Devcore)](http://devco.re/blog/2014/06/19/client-ip-detection/) （使用者 IP、User-Agent 可以竄改）
