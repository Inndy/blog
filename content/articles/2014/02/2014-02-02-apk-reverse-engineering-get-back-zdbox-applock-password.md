---
layout: post
title: APK逆向經驗：取回正點工具箱程式鎖密碼
date: 2014-02-02 07:12
comments: true
categories:
---


### 過程中使用到的工具：

* Python
	* 因為我要從幾百個檔案中，找出其中一個包含有指定字串的檔案...[http://python.org/][1]
  * ~~這樣真的很蠢，請愛用 `find` `grep`~~ (thanks to Orange)
* onekey-decompile-apk
	* APK拖進去就給你Java Code[http://code.google.com/p/onekey-decompile-apk/][2]
* APK multi-tool
	* 我用的是 apk.tw 上，繁體中文化的版本這東西可以解出smali和resource，而且可以打包回APK [https://github.com/APK-Multi-Tool/APK-Multi-Tool][3] [http://apk.tw/thread-217838-1-1.html][4]
* Notepad++
	* Windows下超讚的文字編輯器，因為APK multi-tool linux版好像怪怪的，只好用Windows [http://notepad-plus-plus.org/][5]
* 一支 Root 過的手機
	* 其實可以用模擬器替代啦...
	* [![xperia-sl-hero-black-1240x840-846460e0dc616cc64025fc40df13a6db.jpg](images/2014-02-02-apk-reverse-engineering-get-back-zdbox-applock-password--f813d177--xperia-sl-hero-black-1240x840-846460e0dc616cc64025fc40df13a6db.jpg)][6]
* adb
	* [http://developer.android.com/tools/help/adb.html][7]

<!--more-->

### 第一步：把apk抓出來

```
  Microsoft Windows [版本 6.1.7601]
  Copyright (c) 2009 Microsoft Corporation. All rights reserved.

  C:\Users\Inndy>adb shell
  shell@android:/ $ su
  su
  root@android:/ # cd data/app
  cd data/app
  root@android:/data/app # ls | busybox grep -e 'zd'
  ls | busybox grep -e 'zd'
  com.zdworks.android.toolbox-1.apk
  root@android:/data/app # exit
  exit
  shell@android:/ $ exit
  exit

  C:\Users\Inndy>adb pull /data/app/com.zdworks.android.toolbox-1.apk
  2875 KB/s (6326169 bytes in 2.148s)

  C:\Users\Inndy>
```

### 第二步：分別丟進兩種工具反編譯

### 第三步：找出關鍵字串和參考點

從 APK multi-tool 解出來的東西裡面找，String Resource在 res\values-zh-rTW\strings.xml 裡面，搜尋 "密碼錯誤" 後找到...

`Line 309: <string name="input_fail">密碼錯誤請重新輸入!</string>"`
然後我寫了一個Python Script去找含有 "input_fail" 的檔案，藉此挖出Resource ID

``` python
import os

for root, dirs, files in os.walk("./smali"):
    for f in files:
        f = os.path.realpath("%s/%s" % (root, f))
        if os.path.isfile(f):
            content = open(f, "r").read()
            if content.find("input_fail") > -1:
                print(f)
                for (i, line) in enumerate(content.split("\n")):
                    if line.find("input_fail") > -1:
                        print("Line %5d:%s" % (i + 1, line))

"""
=== Result ===

C:\Users\Inndy\Desktop\APK Multi-Tool V1.0.11\projects\zdbox.apk\smali\com\zdworks\android\toolbox\R$string.smali
Line  1966:.field public static final input_fail:I = 0x7f090342
"""
```
接著在onekey-decompile-apk解出來的source裡面尋找檔名：applock
會找到很多檔案，全部丟進Notepad++打開
搜索所有檔案 -> "2131297090"  (2131297090 = 0x7f090342)
接著找到了...
```
  C:\Users\Inndy\Desktop\zdbox.apk.src\com\zdworks\android\toolbox\ui\applock\AppLockPasswordActivity.java (1 hit)
 Line 109:       Toast.makeText(this, getString(2131297090), 0).show();
  C:\Users\Inndy\Desktop\zdbox.apk.src\com\zdworks\android\toolbox\ui\applock\ApplockPatternActivity.java (1 hit)
 Line 348:           Toast.makeText(ApplockPatternActivity.this, 2131297090, 0).show();
```
接下來就是Code Review找來源
``` java
// com\zdworks\android\toolbox\ui\applock\AppLockPasswordActivity.java
// Line 340
public void onPatternDetected(List<LockPatternView.Cell> paramList)
{
  String str = PasswordUtils.patternToString(paramList);
  ApplockPatternActivity.this.mHandler.postDelayed(new ApplockPatternActivity.AutoClearThread(ApplockPatternActivity.this, null), 1000L);
  if (this.crtPattern.equals(str))
 if ((!ApplockPatternActivity.this.checkpattern(str)) && (ApplockPatternActivity.this.calledIntent != 0) && (ApplockPatternActivity.this.calledIntent != 4))
 {
   ApplockPatternActivity.this.setPatternState(false);
   Toast.makeText(ApplockPatternActivity.this, 2131297090, 0).show();
   ApplockPatternActivity.this.initTitle();
 }
  while (true)
  {
 return;
 ApplockPatternActivity.this.setPatternState(true);
 ApplockPatternActivity.this.finishInputPassword(str);
 continue;
 this.crtPattern = str;
  }
}
```

``` java
// com\zdworks\android\toolbox\ui\applock\ApplockPatternActivity.java
// Line 199
public boolean checkpattern(String paramString)
{
  return paramString.equals(this.patternPassword);
}


// Line 181
private void initView()
{
  initRecommendZDLockView();
  this.patternPassword = this.mConfig.getApplockPasswordPattern();
  this.mLockView = ((LockPatternView)findViewById(2131427460));
  this.mForgetPassword = ((LinearLayout)findViewById(2131427459));
  this.mLockView.setOnPatternListener(new ApplockPatternListener(null));
  if ((-1 != this.mConfig.getSecurityQuestionIndex()) && (this.calledIntent != 0) && (this.calledIntent != 4))
  {
    this.mForgetPassword.setVisibility(0);
    ((TextView)findViewById(2131427799)).getPaint().setFlags(9);
    this.mForgetPassword.setOnClickListener(this);
  }
  this.mLockView.enableInput();
  this.mLockView.setInStealthMode(this.mConfig.isHideTrace());
  this.mLockView.setInVibrateMode(this.mConfig.isVibrateTracelessUnlock());
}


// Line 54
private ConfigManager mConfigManager;
```

``` java
// com\zdworks\android\toolbox\global\ConfigManager.java
// Line 377
public String getApplockPasswordPattern()
{
  return this.mSharedPre.getString("applock_pw_pattern", "");
}


// Line 219
private ConfigManager(Context paramContext)
{
  this.mContext = paramContext;
  this.mSharedPre = PreferenceManager.getDefaultSharedPreferences(paramContext);
}
```

跟到最上面發現原來是[PreferenceManager][8]，可以去把我的密碼找出來了！

```
Microsoft Windows [版本 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Inndy>adb shell
shell@android:/ $ su
su
root@android:/ # cd data/data
cd data/data
root@android:/data/data # ls | busybox grep -e 'zd'
ls | busybox grep -e 'zd'
com.zdworks.android.toolbox
root@android:/data/data # cd com.zd*
cd com.zd*
root@android:/data/data/com.zdworks.android.toolbox # ls
ls
cache
databases
files
lib
shared_prefs
root@android:/data/data/com.zdworks.android.toolbox # cd sh*
cd sh*
root@android:/data/data/com.zdworks.android.toolbox/shared_prefs # ls
ls
GetJarClientPrefs.xml
com.zdworks.android.toolbox_preferences.xml
com.zdworks.android.toolboxsession.xml
lastUsageCheckFile.xml
splash_hash.xml
splash_pref.xml
timestamp.xml
zda_agent_online_setting_com.zdworks.android.toolbox.xml
root@android:/data/data/com.zdworks.android.toolbox/shared_prefs # cat com.zdwor
ks.android.toolbox_preferences.xml | busybox grep -e 'applock_pw_pattern'
<string name="applock_pw_pattern">*******</string>
root@android:/data/data/com.zdworks.android.toolbox/shared_prefs #
```

搞定了，結案。


**最後小提醒：保護手機安全，請隨手關閉adb，並且把adb shell的 root 權限設定為每次詢問。**

[1]: http://python.org/
[2]: http://code.google.com/p/onekey-decompile-apk/
[3]: https://github.com/APK-Multi-Tool/APK-Multi-Tool
[4]: http://apk.tw/thread-217838-1-1.html
[5]: http://notepad-plus-plus.org/
[6]: http://api.sonymobile.com/files/xperia-sl-hero-black-1240x840-846460e0dc616cc64025fc40df13a6db.jpg
[7]: http://developer.android.com/tools/help/adb.html
[8]: http://developer.android.com/reference/android/preference/PreferenceManager.html
