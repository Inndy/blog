---
layout: post
title: 如何刷HTC Flyer P512的ROM（CyanogenMod10）
date: 2014-02-01 12:10
comments: true
categories: 
---
工科技藝競賽的時候入手了一台很難用的HTC Flyer P512  
天啊...Android 3.X是要給鬼用喔  
於是Google了很久終於找到了可以用的ROM，而且是CM10唷！  
雖然還不夠完美，但總比繼續用3.X的Android好 T^T  
  
關於Locked, Unlock, Relock保固差異的說明請見這篇：[http://www.mobile01.com/topicdetail.php?f=566&t=3324387][1]  
  
簡單來說：Locked有完整保固，Unlocked無保固，Relocked部份保固  
**自行斟酌再行刷機**  
  

1. HTC Official Unlock：[http://www.htcdev.com/bootloader][2]
2. 刷CWM：[http://forum.xda-developers.com/showthread.php?t=1775840][3]
3. ROM網址：[http://forum.xda-developers.com/showthread.php?t=1795342][4]  
   把zip放進SD卡，用CWM install from zip
4. 刷完ROM之後，請把boot.img（裏面有兩個，我忘了是哪一個，我沒有S-OFF）解出來，自行刷入  
   `fastboot flash boot boot.img`
5. Google APPs：[http://goo.im/gapps/gapps-jb-20121011-signed.zip][5]

  



[1]: http://www.mobile01.com/topicdetail.php?f=566&t=3324387
[2]: http://www.htcdev.com/bootloader
[3]: http://forum.xda-developers.com/showthread.php?t=1775840
[4]: http://forum.xda-developers.com/showthread.php?t=1795342
[5]: http://goo.im/gapps/gapps-jb-20121011-signed.zip