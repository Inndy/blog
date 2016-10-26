---
layout: post
title: Python對於Encoding的鳥事
date: 2014-05-19 13:20
comments: true
categories:
---
我寫了一個script去parse[這個東西](http://www.shute.kh.edu.tw/~t1248/voc.htm)....

一開始是這麼寫的

``` python
# -*- coding: utf-8 -*-
import requests, re

urls = """http://www.shute.kh.edu.tw/~t1248/voc7000-AB.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - CD.htm
http://www.shute.kh.edu.tw/~t1248/voc7000- EF.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - GHIJ.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - KLM.htm
http://www.shute.kh.edu.tw/~t1248/voc7000 - N O.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - PQR.htm
http://www.shute.kh.edu.tw/~t1248/voc7000 - ST.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - UVWXYZ.htm""".split("\n")

for url in urls:
    content = requests.get(url).content.decode("big5").encode("utf-8")
    # 以下省略
```

過程中遇到了一個 `裏` 字(`'\xF9\xD8'`)，結果python就error了
上Facebook抱怨了一下，就有人告訴我改用`str.decode("cp950")`

[Wikipeida 對於Big5和CP950是這麼說的...](http://en.wikipedia.org/wiki/Code_page_950)

```
The major difference between code page 950 and Big5 is the incorporation of some ETEN characters at F9D6-F9FE (碁, 銹, 裏, 墻, 恒, 粧, and 嫺) and 34 box drawing characters and block elements.
```

結果我剛剛好被這幾個特例給雷了

果然 `裏` 字順利解決，但是又遇到一個`'\x92\xF4'`，有沒有必要這樣整我啊
Firefox上顯示的是 `寝` ，最後跑去查 [UNIHAN](ftp://ftp.unicode.org/Public/UNIDATA/Unihan.zip)，
才發現了 `U+5ACF	kHKSCS	92F4` ，原來是HKSCS
我有種被惡整的了感覺 OTZ

``` python
# -*- coding: utf-8 -*-
import requests, re

urls = """http://www.shute.kh.edu.tw/~t1248/voc7000-AB.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - CD.htm
http://www.shute.kh.edu.tw/~t1248/voc7000- EF.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - GHIJ.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - KLM.htm
http://www.shute.kh.edu.tw/~t1248/voc7000 - N O.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - PQR.htm
http://www.shute.kh.edu.tw/~t1248/voc7000 - ST.htm
http://www.shute.kh.edu.tw/~t1248/voc 7000 - UVWXYZ.htm""".split("\n")

for url in urls:
    content = requests.get(url).content.decode("hkscs").encode("utf-8")
    # 以下省略
```
