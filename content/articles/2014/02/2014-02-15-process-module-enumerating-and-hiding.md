---
layout: post
title: 找出所有已經載入的DLL以及隱藏已經載入的DLL
date: 2014-02-15 12:20
comments: true
categories:
---


從PEB結構體裡面找出所有已經載入的DLL，以及隱藏的方法
可以用在什麼地方就不解釋了....XD

參考資料：

* [http://bbs.pediy.com/showthread.php?t=124325][1] （看雪學院 ）
* [http://msdn.moonsols.com/][2] （裡面有很多 Windows Structures 的資料）

原文是 masm 寫的，我用 C++ 寫了一個

![Q7I6zge.png](/images/2014-02-15-process-module-enumerating-and-hiding--f6e57768--Q7I6zge.png)

（不知道為什麼副檔名.c餵給cl就編不過了...Q____Q，所以說是C++）

<!--more-->

隱藏的部分大概就斷Link、抹除DLL Name和DLL Path、抹掉PE signature
缺點是可能會造成DLL重載、GetModuleHandle抓不到
（反正就說要隱藏了嘛哈哈哈哈）
不過應該還沒有完全隱藏起來，GetModuleHandle還是會掃過...明明Link都斷掉了阿 OTZ
後來發現不能把整個structure給填0，後面如果用到GetModuleHandle會crash
發生的記憶體存取錯誤的地方也附上了，但是有點懶得繼續追
如果有人找到GetModuleHandle用的Link在哪裡的話記得告訴我

Source: [https://gist.github.com/Inndy/d9d1d37221a3a99a3c71][4]
<script src="https://gist.github.com/Inndy/d9d1d37221a3a99a3c71.js"></script>


[1]: http://bbs.pediy.com/showthread.php?t=124325
[2]: http://msdn.moonsols.com/
[3]: http://i.imgur.com/Q7I6zge.png
[4]: https://gist.github.com/Inndy/d9d1d37221a3a99a3c71
