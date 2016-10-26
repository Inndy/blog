---
layout: post
title: Logdown Hacks
date: 2014-05-11 09:28
comments: true
categories: 
---
# Routing Bug

我從blogger匯入文章，但是custom url內有`.`的出現，結果就噴Error 404

## 解決方法

> `http://logdown.com/account/posts/198288-what-is-reset.css/edit`
> `http://logdown.com/account/posts/198288/edit`

進入編輯後，把dot拿掉即可

![dot-in-custom-url](http://i.imgur.com/t1ios3s.png)

<!--more-->

# 大量刪除分類

吐嘈：POST轉頁超慢的，我剛剛從亂七八糟的blogger搬家過來，刪categories刪到吐血

``` js
// ==UserScript==
// @name        ajax-delete-categories
// @namespace   logdown.com
// @include     http://logdown.com/account/blogs/inndy/categories
// @include     https://logdown.com/account/blogs/inndy/categories
// @grant       none
// ==/UserScript==
$('table > tbody > tr > td > button[data-method=delete]') .click(function (e) {
    var $this = $(this);
    if (confirm($this.attr('data-confirm'))) {
        $.ajax({
            'url': $this.attr('data-url'),
            'type': 'post',
            'data': {
                '_method': 'delete',
                'authenticity_token': $('meta[name=csrf-token]') .attr('content')
            },
            'success': function () {
                $this.parent() .parent() .remove();
            }
        });
    }
    e.preventDefault();
    return false;
});
```
