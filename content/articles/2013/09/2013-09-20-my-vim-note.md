---
layout: post
title: 我的vim筆記
date: 2013-09-20 13:37
comments: true
categories: 
---
```
 goto start  
     [[  
 goto end  
     ]]  
 goto 1st line  
     gg  
 goto {N} line  
     {N}G  
 goto last line  
     GG
 goto first character of line  
     0  
 goto last character of line  
     $  
 search  
     /string  
 next match  
     n  
 prev match  
     N  
 multiple {str} {N} times  
     {N}i{string} ESC  
 auto indent lines below
     =G  
 insert after  
     o  
 insert before  
     O  
 remove character  
     x  
 repeat last command  
     .
 replace {A} with {B} in line {M} to {N} ('g' stands for replace all)  
    :{M},{N}s/{A}/{B}/g  
 replace {A} with {B} in all lines
     :%s/{A}/{B}
```