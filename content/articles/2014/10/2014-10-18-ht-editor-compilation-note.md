---
layout: post
title: ht editor 編譯筆記
date: 2014-10-18 13:58
comments: true
categories:
---
最近發現有 [ht editor](http://hte.sourceforge.net/) ，於是想下載編譯來用
無奈奮鬥了半小時還是搞不定，差點就放棄直接載 sourceforge 上的 binary 來用，所幸最後還是搞定了

``` sh
# if you are not use debian family, install dependency on your own
sudo apt-get install autoconf automake libncurses-dev texinfo byacc flex
git clone --depth 1 https://github.com/sebastianbiallas/ht.git
cd ht
./autogen.sh
./configure
make
make htdoc.h
make
sudo make install
```
