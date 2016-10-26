---
layout: post
title: VMProtect 弱保護脫殼小記
date: 2016-09-18 14:33
comments: true
categories: 
---
最近開始玩某個遊戲的私服，世界各國代理商全倒光之後就有一群人在臺港澳中開了私服，甚至就直接用那個遊戲的名字直接營運.... XD

遊戲主程式有加殼，因為有改過所以沒辦法直接從 section name 或是 exeinfoPE 看出來，後來是 ProtectionId 說他是 VMProtect 2.06（我沒辦法驗證這件事情，基本上他沒開任何 VMProtect 的保護功能）

一開始不知道怎麼脫，x64dbg 配 Win10 的環境也不太好作業，所以就在遊戲跑起來的狀況下 dump memory 然後修 IAT，結果 Win10 因為相容性問題，所以引入了 AcLayers.dll / apphelp.dll ，並且在 PE loader 內去 hook EAT，結果就會讓 Scylla 壞掉

![](http://i.imgur.com/z21L8Ky.png)
![](http://i.imgur.com/FCfmayt.png)

脫殼請在該應用程式支援的最低作業系統版本下進行 XD

總之我就先把這樣的 binary 丟進 IDA 看呀看，後來看到一個 function 在 parse commandline（而且 直接把 GetCommandLineA 為給 sscanf，會 overflow呢 XDDDDD），結果就不小心找到 OEP 了

（VC 編譯出來的 OEP 會是一個 call 緊接著一個 opcode = 0xe9 的 jmp，jmp 的目標裡面會有 GetCommandLineA，接著再往下就會呼叫 WinMain）

後來開了 Windows XP VM，OllyDbg + StrongOD，但是 hardware breakpoint 一直被吃掉，大概是 anti-debug 的功能吧，後來用 PhantOm 也沒辦法處理，後來看到其他 VMP 脫殼都說先 break 在 VirtualProtect （沒辦法，packer 注定要用的 API XDDD），按個幾次 F9 直到看到 protection attribute 是 PAGE\_READONLY 為止，現在你的 binary 應該就 decrypt / decompress 完成了，接著去 break OEP，再 F9 就可以 dump 了

接著做出來的 binary 沒辦法執行，會跳 Runtime Error: R6002，查了一下之後在看雪找到解答，Microsoft 的 runtime library 會看某個 section 的 protection attribute，如果可寫就跳過 floating point 相關的 initialization，所以要手動 patch 讓他別跳過（或是也可以設定好正確的 PE section）

最後詳情就請見[看雪論壇](http://bbs.pediy.com/showthread.php?t=81974#post577918)，照著做patch 完就可以動了！

結論：VMProtection 保護都不開的話基本上脫殼難度只比 asprotect 難一點 XDDDD

看了其他人的分析，在開啟 IAT protection 的狀況下真的很麻煩，不過感覺用 binary instrumentation 的技術去處理 IAT reconstruction 應該蠻有幫助的 XD