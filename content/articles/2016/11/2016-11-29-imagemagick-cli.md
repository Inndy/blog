Title: ImageMagick 命令工具
Date: 2016-11-29 16:21
Modified: 2016-11-29 16:21
Category: ImageMagick
Tags: imagemagick, cli

轉換圖片格式：

`convert a.bmp b.png`

破壞壓縮（範圍 1 ~ 100，越高品質越好檔案越大）：

`convert a.bmp -quality 50 b.jpg`

拼接圖片（水平方向）：

`convert 1.png 2.png 3.png +append out.png`

拼接圖片（垂直方向）：

`convert 1.png 2.png 3.png -append out.png`

製作 GIF：

`convert -delay 120 -loop 0 *.png animated.gif`

分解動畫 GIF：

`convert animation.gif +adjoin splitted_%03d.png`

## 組合技！

分解 GIF 然後拼在一起：

`convert 2016-11-29-how-does-qrcode-works.gif +adjoin -append zzz.png`

其他的想到再寫 XD
