---
layout: post
title: reset.css？normalize.css？可以吃嗎？
date: 2013-09-15 12:38
comments: true
categories:
---
好不容易寫好了一份CSS。換個Browser突然獵奇了？IE傲嬌不聽話欠調教？
不同的Browser間會產生差異是因為，各家CSS預設值並不相同
Ex：

> Browser A裡面，div的padding預設是6px
> Browser B裡面，div的padding預設是4px

這時候如果你寫的CSS對齊的很精準...換個Browser就哭哭了！
所以我們透過重新定義所有元素的預設值，不使用瀏覽器的預設值，就可以讓他們乖乖聽話了！

## 說好的載點呢？

[https://github.com/necolas/normalize.css](https://github.com/necolas/normalize.css)

## reset.css如何？

reset.css會把所有element預設的padding, margin, ...全部變成0，font-size全部100%，還要自己手動調整，其實有點麻煩

normalize.css是給你一個共同的default，你就不需要重新定義heading的font-size，不用重新定義p的line-height，比較節省時間。
