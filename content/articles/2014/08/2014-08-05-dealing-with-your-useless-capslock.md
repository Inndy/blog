---
layout: post
title: 處理你無用的CapsLock
date: 2014-08-05 11:39
comments: true
categories:
---
有在用VIM的人應該會覺得ESC好遠好難按，Caps Lock根本用不到
或是emacs的使用者應該會覺得Ctrl的位置很不方便
這時候我們就可以把Caps Lock改成ESC或是Ctrl

對於X Window環境我們可以直接用 `xmodmap` 來解決，至於Mac OS X則要透過Seil這個軟體來解決

## X Window

``` shell
xmodmap -e "keycode 66 = Escape NoSymbol Escape"
```

## Mac OS X

[Seil ( https://pqrs.org/osx/karabiner/seil.html.en )](https://pqrs.org/osx/karabiner/seil.html.en)
