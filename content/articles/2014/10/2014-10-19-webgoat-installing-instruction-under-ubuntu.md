---
layout: post
title: WebGoat installing instruction under Ubuntu
date: 2014-10-19 12:52
comments: true
categories:
---
# WebGoat installing instruction

_you can run this tutorial under any debian family distro but not other platform_

1. `sudo apt-get install tomcat7 tomcat7-admin`
2. `sudoedit /etc/tomcat7/tomcat-users.xml`
3. edit `tomcat-users.xml` like below
4. `sudo service tomcat7 force-reload`
5. open `http://your-server.net:8080/manager/html` and upload your war file
6. open `http://your-server.net:8080/WebGoat-X.X` and enjoy your hack.
   (admin interface will show the path)

## tomcat-users.xml configure example

tomcat-users.xml should looks like below

``` xml
<?xml version='1.0' encoding='utf-8'?>
<!--
  ...
-->
<tomcat-users>
<!--
  ...
-->
  <role rolename="manager-gui"/>
  <user username="admin" password="admin" roles="tomcat,admin-gui,manager-gui,webgoat_user,webgoat_admin"/>
  <user username="guest" password="guest" roles="tomcat,webgoat_user,guest"/>
</tomcat-users>
```
