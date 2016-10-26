---
layout: post
title: Obtain desktop path with batch
date: 2013-02-04 12:25
comments: true
categories:
---
_I havn't tested this in Windows 8 yet._

``` batch
	@echo off
	call :GetDesktop
	echo desktop path = %desktop%
	goto :EOF


	:GetDesktop
	reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v Desktop | find "Desktop" > o.txt
	for /F "tokens=2 delims=\" %%a in (o.txt) do set "desktop=%userprofile%\%%a"
	del o.txt
	goto :EOF
```
