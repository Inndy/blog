---
layout: post
title: [C#]路徑搜索演算法（DFS、BFS）、Flood Fill（Recursive）
date: 2013-09-02 07:00
comments: true
categories:
---

[![%E6%9C%AA%E5%91%BD%E5%90%8D.png](/images/2013-09-02-path-searching-algorithm-with-dfs-and-bfs--2309aeb3--noname.png)][1]

[點我下載 C# 專案][2]

> 操作方式：
> 按住Z, X, C + 滑鼠點擊 / 拖曳
> 可以清除、設定起點、設定終點

這裡用到了兩個容器：Stack 和Queue

Stack的操作：Push （推入） / Pop （取出）
Stack的操作特性：有底容器

[![real_stack.png](/images/2013-09-02-path-searching-algorithm-with-dfs-and-bfs--030604d2--real_stack.png)][3]

像是一個有底容器，同一層只能有一個物件存在，先放進去的東西比較晚出來，比較晚放進去的東西先出來


Queue的操作：Enqueue （排入） / Dequeue （取出）
Queue的操作特性：排隊

[![queue.png](/images/2013-09-02-path-searching-algorithm-with-dfs-and-bfs--485a3e0e--queue.png)][5]


[1]: http://1.bp.blogspot.com/-8IrpqNgo0XI/UiPg2vc7frI/AAAAAAAABjs/Dal5UEY8A2o/s1600/%E6%9C%AA%E5%91%BD%E5%90%8D.png
[2]: https://dl.dropboxusercontent.com/u/644586/SearchPath.7z
[3]: http://2.bp.blogspot.com/-ztf-qRp6HnE/UiPi9-UfOFI/AAAAAAAABkA/K-_UKXwT-jc/s1600/real_stack.png
[4]: http://3.bp.blogspot.com/-B_ji2xeZHiw/UiQ3BcqvynI/AAAAAAAABkQ/fVT2_T-EXzQ/s320/queue.png
[5]: http://3.bp.blogspot.com/-B_ji2xeZHiw/UiQ3BcqvynI/AAAAAAAABkQ/fVT2_T-EXzQ/s1600/queue.png
