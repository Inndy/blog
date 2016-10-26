---
layout: post
title: 把M$ Excel的Sheets切成不同檔案
date: 2014-09-07 17:34
comments: true
categories: 
---
今天被問了奇怪的問題，覺得有價值筆記下來，VBA不解釋

``` vb split-sheets-to-files.vbs
Sub Main()
    If MsgBox("Hi, Split sheets to files?", vbYesNo) = vbNo Then Exit Sub
    Dim xPath As String
    xPath = Application.ActiveWorkbook.Path
    Application.ScreenUpdating = False
    Application.DisplayAlerts = False
    For Each xWs In ThisWorkbook.Sheets
        xWs.Copy
        Application.ActiveWorkbook.SaveAs Filename:=xPath & "\" & xWs.Name & ".xls"
        Application.ActiveWorkbook.Close False
    Next
    Application.DisplayAlerts = True
    Application.ScreenUpdating = True
    MsgBox "Done! Files are in..." & vbNewLine & Application.ActiveWorkbook.Path
End Sub
```