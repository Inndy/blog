---
layout: post
title: 重灌Windows之後，修復Linux Mint（Ubuntu）的開機選單（grub2）
date: 2013-11-17 08:43
comments: true
categories: 
---
我的筆電有裝雙系統，Windows 7和Linux Mint
（當然，Ubuntu也適用同樣的方法）  
昨天我重灌了Windows 7，所以需要重建grub2  
上網找了很多東西之後，分享一下我成功的方法  
  
先用 Live CD 或是 Live USB 開機，然後打開terminal  
  
```
	# 我的mint在sda3，/boot沒有另外mount  
	mount /dev/sda3 mnt  
	sudo mount --bind /dev /mnt/dev  
	# 如果你的/boot有另外mount  
	#sudo mount --bind /boot /mnt/boot  
	sudo mount --bind /dev/pts /mnt/dev/pts  
	sudo mount --bind /proc /mnt/proc  
	sudo mount --bind /sys /mnt/sys  
	sudo chroot /mnt/  
	# 我的boot hdd在sda  
	grub-install /dev/sda  
	update-grub  
```
finally... sudo reboot and enjoy your Linux Mint :D  
  
參考文獻：[http://wiki.ubuntu-tw.org/index.php?title=GRUB2%E4%B8%AD%E6%96%87%E6%8C%87%E5%8D%97%E7%AC%AC%E4%BA%8C%E7%89%88%28%E4%B8%8A%EF%BC%89#.E6.96.B9.E6.A1.88_3_-_CHROOT][1]

[1]: http://wiki.ubuntu-tw.org/index.php?title=GRUB2%E4%B8%AD%E6%96%87%E6%8C%87%E5%8D%97%E7%AC%AC%E4%BA%8C%E7%89%88%28%E4%B8%8A%EF%BC%89#.E6.96.B9.E6.A1.88_3_-_CHROOT