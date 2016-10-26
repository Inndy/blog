---
layout: post
title: Bypassless Cheat Script (ICS) Updating
date: 2012-08-03 22:59
comments: true
categories: 
---
## Demo Script

```
// TWMS146.3 ICS Walking Mob Falling
[ENABLE]
00BC7AC8:
DD 008EB461
[DISABLE]  
00BC7AC8:
DD 008F352D
```

```
// TWMS147.4 ICS Walking Mob Falling
[ENABLE]  
00C32DF0:  
DD 009424F5  
[DISABLE]  
00C32D70:  
DD 0094A963
```
 

## How to update?
```
// TWMS146.3 ICS Walking Mob Falling
[ENABLE]  
00BC7AC8:  
DD 008EB461 // signature update
[DISABLE]  
00BC7AC8:   // 4bytes scan 008F352D
DD 008F352D // signature update
```