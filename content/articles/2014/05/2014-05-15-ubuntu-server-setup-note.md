---
layout: post
title: Ubuntu Server Setup Note
date: 2014-05-15 13:46
comments: true
categories: 
---
# Config


## Default Editor For sudoedit

`sudo update-alternatives --config editor`

## Static IP

`sudoedit /etc/network/interfaces`

``` text /etc/network/interfaces
auto eth0
iface eth0 inet static
address <address>
netmask <mask>
network <network>
broadcast <broadcast>
gateway <gateway>
dns-nameservers 8.8.8.8
```


# Problems


## sendmail was slow

``` text /etc/hosts
127.0.0.1		localhost localhost.localdomain myservername myservername.localdomain
```


# Server


## Apache with PHP

```
sudo apt-get install apache2
sudo apt-get install php5
sudo apt-get install libapache2-mod-php5
```


# Security


## fail2ban

`sudo apt-get install fail2ban`

## Knock Knock

Use [Knock-Knock](http://codecapsule.com/2010/07/06/knock-knock-secure-your-ssh-server-using-port-knocking/) to security ssh