---
layout: post
title: SSH tunnel 筆記
date: 2016-02-26 08:14
comments: true
categories: 
---
SSH Tunnel 有**三種**工作模式，使用 ssh tunnnel 的好處有：

- 在可能被監聽的網路環境保護未加密連線的安全
- 翻牆
- 一定程度上取代 VPN，是一個比較 light-weight 的解決方案

## 先定義兩個名詞：

- local: ssh client
- remote: ssh server

### 在 local listen port A，透過 remote forward 到 host B 的 port C

`ssh user@host -L [local_bind_address:]local_port_A:host_B:remote_port_C`

example:

`ssh user@host -L 8080:10.7.99.8:80` -- 在 local 聽 8080 port，透過 remote 再連到 `10.7.99.8:80`

### 在 remote listen port A，透過 local forward 到 host B 的 port C

`ssh user@host -R [remote_bind_address:]local_port_A:host_B:remote_port_C`

example:

`ssh user@host -R 2223:140.112.172.1:23` -- 在 remote 聽 2223 port，透過 local 再連到 telnet protocol 的 ptt

### 在 local listen port P，建立 socks proxy server

`ssh user@host -D [local_bind_address:]local_port_P`

example:

`ssh user@host -D 7788` -- 在 local 聽 7788 port，會是一個 socks proxy service，連線會透過 remote 再連到目標