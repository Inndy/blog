---
layout: post
title: Concurrency? Parallel?
date: 2015-12-08 08:52
comments: true
categories: 
---
平行化處理大家應該都耳熟能詳，舉例來說 multi-threading 和 multi-processing 都屬於平行化（parallel），至於 parallel 的定義如下：

> 在「同一個時間點」有「多個工作在執行」

那麼 concurrency 呢？

> 兩個工作起始到結束的時間區間有重疊

舉例來說：我開了 10 個 thread 的網頁爬蟲去爬 PTT 表特版，這屬於 parallel，也屬於 concurrency

又或者：透過 `pthread` 函式庫用 C 語言實作的 merge sort ，屬於 parallel 也屬於 concurrency

但是 single thread 做 context-switch 則算是 concurrency

e.g. Python 的 `threading` 模組，因為 [GIL](https://zh.wikipedia.org/zh-tw/GIL) 的關係，所以同一時間只會有一個 threading 在 Python interpreter 裡面運作

