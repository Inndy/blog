---
layout: post
title: iptables筆記
date: 2014-05-24 02:44
comments: true
categories: 
---
``` shell iptables-setup.sh
#!/bin/bash

if [ $UID -ne 0 ]; then
	sudo $0 $*
	exit
fi

# Clear default rules
iptables -F
iptables -X
iptables -Z

# Default policy for INPUT
iptables -P INPUT DROP

# Accept for loopback
iptables -A INPUT -i lo -j ACCEPT

# Allow ssh, http
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT

# Do not drop packet from established connection
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

# List
iptables -L -n -v
```

``` shell
sudo cp iptables-setup.sh /etc/init.d/
sudo chown root:root /etc/init.d/iptables-setup.sh
sudo chmod 755 /etc/init.d/iptables-setup.sh

# Use your own runlevel, runlevel = 2 for Debian family distro
sudo ln -s /etc/init.d/iptables-setup.sh /etc/rc2.d/S90iptables-setup
```