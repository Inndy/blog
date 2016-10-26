---
layout: post
title: Classes in JavaScript
date: 2013-11-30 15:41
comments: true
categories: 
---


是的，你沒有看錯，JavaScript也有class  
JS的物件，本質上是dictionary，但是有個奇怪的東西叫做prototype，也可以定義constructor  
下面就來示範一個空的Class  
  

	function ClassA() { }  
	var object1 = new ClassA();  
	console.log(object1 instanceof ClassA); // true  
什麼是dictionary相信大家都知道，至於什麼是prototype呢？我們來舉個例子看看  
  
	function Class1(name) { this.Name = name; }  
	Class1.prototype.func = function () { console.log("this is a new instance of Class1, named " + this.Name); };  
	  
	var obj = new Class1("TestObject");  
	obj.func(); // this is Spada prototype  
簡單來說，就是OOP的method拉！只要是這個function建構出來的object都會有這個method的存在，你也可以透過 Hack String.prototype 來達成自己擴充字串的method  
  
	String.prototype.padLeft = function (l, c) {  
	 c = c || ' ';  
	 var s = this;  
	 while (s.length < l) s = c + s;  
	 return s;  
	};  
	  
	console.log("2".padLeft(5, '0')); // 00002  
  
  
	function People(Name, Age) {  
	    var me = this;  
	    me.name = Name;  
	    var age = Age; // private variable  
	    var getMyName = function () { // private method  
	        return me.name;  
	    };  
	  
	    this.getAge = function () {  
	        return age;  
	    };  
	  
	    this.SayHi = function () {  
	        return "Hi! I'm " + getMyName();  
	    };  
	}  
	  
	People.prototype.toString = function () {  
	    return "A people called " + this.name + " and " + this.getAge() + " years old";  
	};  
	  
	var inndy = new People("Inndy", 17);  
	console.log(inndy.SayHi()); // "Hi! I'm Inndy"  
	  
	// if you compare a string with a object that has a method called 'toString'  
	// it will compare string with object.toString()  
	// you can build 'toString' method in constructor or using prototype  
	console.log(inndy == "A people called Inndy and 17 years old"); // true  
	console.log(inndy === "A people called Inndy and 17 years old"); // false  
	  
	console.log("inndy.toString() -> \"" + inndy.toString() + "\"");

