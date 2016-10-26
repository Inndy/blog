---
layout: post
title: HTML5新鮮小物：Data URI
date: 2012-08-23 07:45
comments: true
categories:
---
## 什麼是Data URI？

網頁中有很多地方要引用其他資源，例如：Script、Frame、Img、Style..etc.，就會輸入資源的URL，Data URI就是把資源的內容Base64 Encode或是URLEncode後，直接寫在URL的地方
Ex:
``` html
<img src="data:image/png,%89%50%4e%47%0d%0a%1a%0a%0d%49%48%44%52%10%10%01%03%25%3d%6d%22%06%50%4c%54%45%ff%ff%ff%a5%d9%9f%dd%33%49%44%41%54%78%9c%63%f8%ff%9f%e1%ff%5f%86%ff%9f%19%0e%b0%33%dc%3f%cc%70%7f%32%c3%cd%cd%0c%37%8d%19%ee%14%83%d0%bd%cf%0c%f7%81%52%cc%0c%0f%c0%e8%ff%7f%51%86%17%28%ce%5d%9b%50%49%45%4e%44%ae%42%60%82">
```

或是

``` html
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC">
```

效果：
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC">

好處：節省Request數量，有時候檔案真的太小了，這樣做比較快
壞處：Client佔用較多CPU、記憶體，還需要一點Decode的時間

特殊別用處：用JavaScript寫插件的時候很好用
Wikipedia: [Data URI scheme](http://en.wikipedia.org/wiki/Data:_URL)
