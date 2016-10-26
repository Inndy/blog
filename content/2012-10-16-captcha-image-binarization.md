---
layout: post
title: CAPTCHA自動辨識前置二值化處理以及簡易雜訊去除
date: 2012-10-16 13:23
comments: true
categories: 
---
看，這個就好欺負了：![][1]  
這個算是中等的：![][2]  
遇到這個算我運氣差...直接放棄比較快XD： ![][3]  
  
對於某些網站想要寫自動化操作程式，卻被CAPTCHA（圖形化驗證碼）阻擋？  
目前最簡單的手段就是交給OCR去識別，但是目前許多小型的OCR Engine功能較不完善，需要由我們來進行二值化  
今天就來看一下二值化該怎麼做！  

## 二值化

首先先來認識一下RGB色彩系統（色加法，光的三原色）  
![][5]  
（上圖取自[Adobe官方網站][6]）  
  
Red, Green, Blue，光的三原色，強度相等疊加起來就會變成白色(#FFFFFF)  
如果全部都沒有那就是黑色(#000000)  
  
那麼，我們只要取色彩濃度的臨界點，去做二值化（非黑即白）即可完成  
  

## 雜訊去除

  
常用的手段無非在背景隨機打點或是隨機背景圖片  
我們以上面的三張範例圖片中的第二張來說，一個很好用的思路：雜訊是獨立的點，面積很小，所以這時候就判斷每個色塊的面積，如果太小則予以移除  
  
  
  

## DEMO

  
在此用C#做個小範例...  
![][7]  
Code:  
  
``` csharp
private void CalcArea(ref Bitmap bm, int x, int y, ref int size )
{
  if (x < 0 || x >= bm.Width || y < 0 || y >= bm.Height) return;
  Color c = bm.GetPixel(x, y);
  if (c.R == 0xff && c.G == 0xff && c.B == 0xff)
  {
    return;
  }
  else
  {
    size++;
    bm.SetPixel(x, y, Color.White);
    CalcArea(ref bm, x - 1, y, ref size);
    CalcArea(ref bm, x, y - 1, ref size);
    CalcArea(ref bm, x + 1, y, ref size);
    CalcArea(ref bm, x, y + 1, ref size);
  }
}

private void btnProcess_Click(object sender, EventArgs e)
{
  Bitmap pic;
  try
  {
    pic = (Bitmap)pbCaptcha.Image;
    if (pic == null)
      return;
  }
  catch (Exception ex) { return; }
  List<Point> lst = new List<Point>();
  for (int x = 0; x < pic.Width; x++)
    for (int y = 0; y < pic.Height; y++)
    {
      Color c = pic.GetPixel(x, y);
      if ((c.R + c.G + c.B) / 3 > 0x60)
        pic.SetPixel(x, y, Color.White);
      else
        pic.SetPixel(x, y, Color.Black);
    }
  for (int x = 0; x < pic.Width; x++)
    for (int y = 0; y < pic.Height; y++)
    {
      Color c = pic.GetPixel(x, y);
      if (c != Color.White)
      {
        int size = 0;
        Bitmap tmp = (Bitmap)pic.Clone();
        CalcArea(ref tmp, x, y, ref size);
        if (size < 60)
        {
          pic.Dispose();
          pic = tmp;
        }
        else
        {
          tmp.Dispose();
        }
      }
    }
  pbCaptcha.Image = (Image)pic;
}
```



[1]: http://2.bp.blogspot.com/-307_e88YtoE/UH1XXqSE8aI/AAAAAAAABHA/m5dhnRrZshA/s1600/01.png
[2]: http://3.bp.blogspot.com/-z9lLwcyPca4/UH1dqEWo8LI/AAAAAAAABHg/FylwvAFRcjw/s1600/04.jpg
[3]: http://1.bp.blogspot.com/-55bAStIYvIs/UH1XYLp9ZcI/AAAAAAAABHI/Cz5GkWdXS2E/s1600/Captcha.jpg
[5]: http://4.bp.blogspot.com/-aspMRWjxZNc/UH1YEBmxrpI/AAAAAAAABHQ/SoFMDBtd4GQ/s320/rgb_model.gif
[6]: http://goo.gl/KPy0b
[7]: http://2.bp.blogspot.com/-kjZ9Pnj6bOM/UH1e04aXX0I/AAAAAAAABHo/aJWyYemU10U/s1600/B8A.png