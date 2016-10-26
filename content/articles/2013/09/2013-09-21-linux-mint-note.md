---
layout: post
title: 我的Linux Mint筆記
date: 2013-09-21 04:47
comments: true
categories: 
---


## root那些大小事

使用root身份相等的權限執行指令  

`sudo <指令>`

把目前的terminal暫時切換到root身份（exit會退回原本的user）  

`sudo -i`
  

## Grub2設定

grub.cfg在  

`/boot/grub/grub.cfg`

但是他是組合出來的，所以要改設定來源，grub目錄本體放在  

`/etc/grub.d`

內容有  

```
00_header  
05_debian_theme  
06_mint_theme  
10_linux  
10_lupin  
20_linux_xen  
20_memtest86+  
30_os-prober  
30_uefi-firmware  
40_custom  
41_custom  
README
```

其中預設項目以及預設讀秒在  

`00_header`

，請加入以下兩行來設定預設項目（從0開始數）和倒數讀秒   

```
# Do this as early as possible, since other commands might depend on it.  
# (e.g. the `loadfont' command might need lvm or raid modules)  
for i in ${GRUB_PRELOAD_MODULES} ; do  
echo "insmod $i"  
done  

GRUB_DEFAULT=0  
GRUB_TIMEOUT=5  

if [ "x${GRUB_DEFAULT}" = "x" ] ; then GRUB_DEFAULT=0 ; fi  
if [ "x${GRUB_DEFAULT}" = "xsaved" ] ; then GRUB_DEFAULT='${saved_entry}' ; fi  
if [ "x${GRUB_TIMEOUT}" = "x" ] ; then GRUB_TIMEOUT=10 ; fi  
if [ "x${GRUB_GFXMODE}" = "x" ] ; then GRUB_GFXMODE=auto ; fi
```

修改完成之後執行  

`sudo update-grub`

來更新grub menu  
  

##  輸入法那些小事

個人推薦以hime來取代gcin，原因很簡單，我覺得hime的icon比gcin的好看！  
hime是從gcin fork出來的一個branch，作者希望收一些gcin不收的patch，以及改進一些bug和UX，分別用過gcin和hime之後，個人覺得hime用起來爽度比較高，不過還是會告訴你gcin怎麼安裝！  

`sudo apt-get install hime # 安裝hime輸入法`

#### 然後然後！！！

* 如果你已經習慣了Windows上的微軟新注音輸入法，建議**_不要_**使用新酷音，採用hime / gcin內，原本就有的 **"詞音"** 輸入法，稍候也會附上文章教你把詞音調教調整成比較接近微軟新注音輸入法的狀態

如果想在hime上使用新酷音的使用者就...  

`sudo apt-get install hime-chewing # 安裝hime的新酷音`

  
想使用gcin的使用者這樣做  

`sudo apt-get install gcin # 安裝gcin輸入法`

gcin上的新酷音   

`sudo apt-get install gcin-chewing # 安裝gcin的新酷音`

  
最後附上一篇文章：[小克's 部落格: 讓Linux下的中文輸入法更接近微軟新注音使用體驗][2]  
對於從Windows跳槽的人應該會有幫助  
  

## 軟體、套件安裝

軟體來源請選這兩個（以台灣來說比較快），而且我遇到很多套件都下載失敗  
  

[![][3]][3]

  

## 文字編輯器

* vim心法
	* [我的vim筆記][4]
* 我的vim設定檔
	* 其實我也不太懂，我只是複製了 [Denny][5] 大大的部份設定檔
	* [https://dl.dropboxusercontent.com/u/644586/vimrc][6]
	* 套用請這樣
	* `wget https://dl.dropboxusercontent.com/u/644586/vimrc -O ~/.vimrc`
		* 底線自動縮排
    * tab寬度=4
    * 搜尋不分大小寫
    * 從目前游標位置開始搜索
    * 顯示目前命令
    * 語言為Python時，以4個Space取代tab進行縮排 
* nano
	* 可以試試看，比較接近windows notepad
* gedit
	* 如果你需要GUI介面！ 如果你沒有用過vi, vim, nano這類文字介面編輯器，可以用這個 
* [emacs][7]
	* 可是Linux Mint並沒有預載sudo apt-get install emacs
* 看看Wikipedia怎麼說
	* http://en.wikipedia.org/wiki/Category:Linux_text_editors



[2]: http://goodjack.blogspot.tw/2013/08/linux-phonetic-setting.html
[3]: http://3.bp.blogspot.com/-iPmuE2rLoyI/Ujx1fHL7ajI/AAAAAAAABk8/ld2WnykPcpM/s1600/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96%E5%AD%98%E7%82%BA+2013-09-21+00:17:40.png
[4]: http://inndyxd.blogspot.tw/2013/09/my-vim-note.html
[5]: http://www.plurk.com/denny0223
[6]: https://dl.dropboxusercontent.com/u/644586/vimrc
[7]: http://www.gnu.org/software/emacs/