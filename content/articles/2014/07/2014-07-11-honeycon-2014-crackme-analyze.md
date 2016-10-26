---
layout: post
title: HoneyCon 2014 CrackMe Analyze
date: 2014-07-11 14:12
comments: true
categories:
---
``` cpp
int __cdecl main() // decompiled with IDA
{
  char *char_ptr; // edi@2
  int val_1; // eax@3
  int val_tmp_1; // edx@3
  char val_tmp_2; // zf@4
  int length; // edi@8
  unsigned int counter_1; // eax@9
  unsigned __int8 v6; // dl@9
  signed int counter_2; // eax@14
  unsigned __int8 table_2[8]; // [sp+18h] [bp-824h]@1
  unsigned int __table_2_2; // [sp+1Ch] [bp-820h]@1
  unsigned __int8 table_1[24]; // [sp+20h] [bp-81Ch]@1
  unsigned int __table_1_2; // [sp+24h] [bp-818h]@1
  unsigned int __table_2_3; // [sp+28h] [bp-814h]@1
  unsigned int __table_2_4; // [sp+2Ch] [bp-810h]@1
  char process_buffer[1024]; // [sp+30h] [bp-80Ch]@11
  char input_buffer[1036]; // [sp+430h] [bp-40Ch]@2

  sub_401C30();
  /*
    unsigned char map_1[] = {
		0x10, 0x7D, 0x33, 0xCE, 0x30, 0xF7, 0x88, 0x3C,
		0x23, 0x02, 0x73, 0xC2, 0x3D, 0xDF, 0xF2, 0x5E
	};
	unsigned char map_2[] = { 0x65, 0x13, 0x00, 0xB8, 0x03, 0xC5, 0xE6, 0x0C };
  */

  *(_DWORD *)table_1 = 0xCE337D10u;
  __table_1_2 = 0x3C88F730u;
  __table_2_3 = 0xC2730223u;
  __table_2_4 = 0x5EF2DF3Du;
  *(_DWORD *)table_2 = 0xB8001365u;
  __table_2_2 = 0xCE6C503u;
  while ( 1 )
  {
    char_ptr = input_buffer;
    printf("Enter key to unlock: ");
    fgets(input_buffer, 1024, (FILE *)iob /* stdin */);

    do {
      val_tmp_1 = *(_DWORD *)char_ptr;
      char_ptr += 4;

      // 這個地方有點特別可以算算看
      // unsigned char b = 0x00;
      // ~b & (b - 0x01) & 0x80 == 0x80
      // 等價於 b ? 0x00 : 0x80
      // 推廣到int32_t
      val_1 = ~val_tmp_1 & (val_tmp_1 - 0x1010101) & 0x80808080;
    } while ( !val_1 );

    // 判斷low-part有沒有東西
    val_tmp_2 = (unsigned __int16)(val_1 & 0x8080) == 0;

    if ( !(val_1 & 0x8080) ) // 如果low-part有東西的話，把hi-part拉到low-part，讓後面繼續判斷
      val_1 = (unsigned int)val_1 >> 16;

    if ( val_tmp_2 ) // 如果low-part有東西的話 +2
      char_ptr += 2;

    // 最後其實就是strlen
    length = &char_ptr[-((_BYTE)val_1 >= (unsigned __int8)-(_BYTE)val_1) - 3] - input_buffer - 1;

    // 基本上這是個無意義操作
    input_buffer[length] = 0;

    if ( length > 0 )
    {
      v6 = 0x10; // 注意囉，first byte的xor key是 0x10
      // 底下看起來很可怕，而且一次 shift 59 bits有點奇怪，背後的 opcode 是：
      // 00403832 sar     ecx, 31
      // 00403835 shr     ecx, 28
      // 這裡先說明一下 sar 這個指令， SAR (Shift Arithmetic Right)
      // 基本上他做的事情是shift right (shr)，但是他會用MSB做填充，即正負不變
      // 用於 signed 操作，至於 shr 則是 shitft right ，空位用 0 填充
      // sar reg, 31 是有特殊意義的，他會用MSB填滿整個register，
      // i.e.: reg = (reg < 0) ? -1 : 0;
      // 接下來的 shr ecx, 28 ，串起來就會變成 reg = (reg < 0) ? 0b01111 : 0;
      // 這時候 & 0x0F 就變成沒有意義的操作了
      // 所以可以化簡成 ((counter_1 + (counter_1 >> 59))) - (counter_1 >> 59)
      // counter_1 + (counter_1 >> 59) - (counter_1 >> 59)
      // 最後就變成 v6 = table_1[counter_1]
      for ( counter_1 = 0; ; v6 = table_1[((counter_1 + (counter_1 >> 59)) & 0xF) - (counter_1 >> 59)] )
      {
        process_buffer[counter_1] = input_buffer[counter_1] ^ v6;
        ++counter_1;
        if ( length == counter_1 )
          break;
      }
      // first byte 是分開處理的
      // first byte = 'e' ^ 0x10 = 'u'
      // 另外由此可知，key length 是 8
      if ( length == 8 && process_buffer[0] == 'e' )
        break; // 這個 break 會出 最外層的 while ( 1 )，就會跳過LABEL_18
    }
LABEL_18:
    puts("Key error, please retry :)");
  }
  counter_2 = 0;
  while ( 1 )
  {
    ++counter_2; // minium counter_2 is 1
    if ( counter_2 > 7 ) // counter_2 -> [1, 7]
      break;
    // counter_2 永遠小於等於 7 ，所以 & 7 也是無意義操作
    // 所以可以知道 input 會先跟 table_1 做 xor 在跟 table_2 比對
    // key[1] ~ key[7] 就是 table_1[i] ^ table_2[i] ， i -> [1, 7]
    if ( process_buffer[counter_2] != table_2[counter_2 & 7] )
      goto LABEL_18;
  }
  puts("Successfully unlock!");
  system("pause");
  return 0;
}
```

Key is `un3v32n0`

Reference: [Intel Pentium Instruction Set Reference (Basic Architecture Overview)](http://faydoc.tripod.com/cpu/)
