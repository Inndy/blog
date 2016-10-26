---
layout: post
title: 某網站小遊戲加密弱點分析
date: 2015-03-30 02:02
comments: true
categories:
---
# 某網站小遊戲加密弱點分析

故事是這樣的，某~~(N)~~大~~(T)~~學~~(U)~~的某系之夜弄了一個網站，上面有幾個 JS + canvas 寫的小遊戲，看到小遊戲我怎麼能夠放過不玩~~（弄）~~呢？

## 先來看看原始 Code

``` js
function Encode_orig(t, n) {
    var i = 'abcdefghijklmnopqrstuvwxyz0123456789{:}"!@.$%,&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ?',
        o = {},
        e = i.length;
    n %= e, 0 == n && (n = 2);
    for (var r = 0; e > r; r++) o[i[r]] = r;
    for (var s = t.split("").map(function(t) {
        return o[t]
    }), r = 0; r < s.length; r++) s[r] = s[r] * n % e;
    return s.map(function(t) {
        return i[t]
    }).join("")
}
```

## 存在問題

1. map 上的第一個 char 不會被換置
2. 完全對稱加密
3. key == 1 時，等於原文
4. key 空間太小（key %= char_map.length），使得 bruteforce 可能

``` js
function Encode(str, key) {
    // the map
    var char_map = 'abcdefghijklmnopqrstuvwxyz0123456789{:}"!@.$%,&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ?';

    key %= char_map.length;

    if (key == 0) {
        key = 2;
    }

    return str.split("").map(function(e) {
        return char_map.indexOf(e);
    }).map(function (e) {
        return e * key % char_map.length;
    }).map(function(e) {
        return char_map[e]
    }).join("");
}

function Decode(str, key) {
    var char_map = 'abcdefghijklmnopqrstuvwxyz0123456789{:}"!@.$%,&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ?';
    var rev_map = Encode(char_map, key);

    return str.split("").map(function(e) {
        return char_map[rev_map.indexOf(e)];
    }).join("");
}

function Bruteforce(str, filter) {
    var r = [];
    for (var i = 2; i < 80; i++) {
        var c = Decode(str, i);
        if (!filter || filter(c)) r.push([i, c]);
    }
    return r;
}

var r = Bruteforce('0pq}SpXpd1YnbYnb9Sbn}t$}Kp,', function (e) {
    // JSON data must starts with '{' or '['
    return e[0] == '{' || e[0] == '[';
});

console.log('Bruteforce result:\n' + r.join('\n') + '\n');

var key = 12345;
var enc = Encode('abcdefghijklmnopqrstuvwxyz0123456789{:}"!@.$%,&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ?', key);
var dec = Decode(enc, key);
console.log("Key: " + key);
console.log("Encoded: " + enc);
console.log("Decoded: " + dec);


function validate() {
    var test_str = [ 'abcdefg', 'asjdfjaklsdf', 'jqjriowjoiasjdf', 'abcdefghijklmnopqrstuvwxyz0123456789{:}"!@.$%,&*()_+ABCDEFGHIJKLMNOPQRSTUVWXYZ?', 'owoasdf123______________' ];
    var test_key = [ 1234567, 223457, 123456789, 12343412, 333333334, 2345, 2, 0 ];
    var result = true;

    test_str.map(function (qq) {
        test_key.map(function (pp) {
            result = result && ( Encode(qq, pp) === Encode_orig(qq, pp) );
        });
    });

    return result;
}

console.log();
console.log('Testing my implement...');
console.log(validate() ? "Test pass" : "Test failed");
```

## 改進建議

1. 使用現有 cryptology library
2. 加強混淆強度
3. ~~這幾個小遊戲真的不太好玩~~
