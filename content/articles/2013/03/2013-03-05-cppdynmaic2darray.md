---
layout: post
title: C++動態二維陣列 / Dynmaic 2D Array in C++
date: 2013-03-05 09:59
comments: true
categories:
---
## code

``` cpp
	#include <cstring> // for memcpy
	#define NEW2D(H, W, T) (T **)new2d(H, W, sizeof(T))
	#define CPY2D(TAR, SRC, H, W, T) cpy2d((void**)TAR, (void**)SRC, H, W, sizeof(T))
	#define DEL2D(P) (delete [] P)

	void cpy2d(void** tar, void** src, int h, int w, int size) {
	 for (register int i = 0; i < h; i++)
	 memcpy(tar[i], src[i], size * w);
	}

	void* new2d(int h, int w, int size)
	{
	 register int i;
	 void **p;
	 p = (void**)new char[h * sizeof(void*) + h * w * size];
	 for(i = 0; i < h; i++)
	 p[i] = ((char *)(p + h)) + i * w * size;
	 return p;
	}
```

## Using Demo...

``` cpp
	int **map = NEW2D(16, 32, int); // Height, Width, Type
	scanf("%d", &map[15][31]);
	printf("%d\n", map[15][31] + 1);
	int **map2 = NEW2D(16, 32, int); // Another 2D array
	CPY2D(map2, map, 16, 32, int); // Copy to another array
	printf("%d\n", map2[15][31] + 2);
	DEL2D(map); // Free meory
	DEL2D(map2);
```

[Reference](http://goo.gl/vMu77)
