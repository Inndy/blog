---
layout: post
title: 回應洋蔥分析文之我也來分析
date: 2012-06-08 10:32
comments: true
categories: 
---
※這是TWMS146.1的位置
TWMS146.1 取得最大經驗值位置分析
小蔥蔥文章原文網址：[按我][1]

| Address  |         Instruction |                                                |
| :------- | :------------------ | :--------------------------------------------- |
| 006A345C |            push eax | 等級                                           |
| 006A345D |       call 006a33e4 | 取得升等所需經驗值                             |
| 006A3462 |    sub eax,[esp+0c] | [esp=0c]是目前經驗值                           |
|          |                     | eax = 所需經驗值-目前經驗值 = 還需要多少經驗值 |
| 006A3466 |             pop ecx | 因為查詢升等所需經驗值的CALL是__cdecl的CALL
|          |                     | （堆疊中放入參數，要由呼叫端清除堆疊內的參數） |
| 006A33E4 |       push [esp+04] | CALL的參數（等級）                             |
| 006A33E8 |    mov ecx,00d3d180 | 經驗值表的位置                                 |
| 006A33ED |       call 006a33c4 | 查詢經驗值表                                   |
| 006A33F2 |                 ret | 返回                                           |
| 006A33C4 |    mov eax,[esp+04] | 取得參數（等級）到EAX                          |
| 006A33C8 |    cmp eax,000000c8 | 判斷[等級]和200                                |
| 006A33CD |         jg 006a33dc | 如果等級大於200則跳到006a33dc                  |
| 006A33CF |          cmp eax,01 | 判斷[等級]和1                                  |
| 006A33D2 |        jnl 006a33d7 | 如果等級大於等於1跳到006a33d7                  |
| 006A33D4 |         xor eax,eax | Eax = 0                                        |
| 006A33D6 |             inc eax | Eax ++                                         |
| 006A33D7 | mov eax,[ecx+eax*4] | 查表（表在00d3d180）                           |
| 006A33DA |        jmp 006a33e1 | 跳到返回                                       |
| 006A33DC |    mov eax,7fffffff | 最大經驗值為 0x7fffffff                        |
| 006A33E1 |            ret 0004 | 返回                                           |


[1]: http://knowlet3389.blogspot.tw/2012/06/twms-v146crc_03.html