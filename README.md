Python script to convert pdf to png or jpeg.  
  
Pythonライブラリの「**pdf2image**」を使って、**pdf_file**内にあるpdfを画像(PEGやPNG)ファイルに一括で変換するスクリプトです。（書き出し先は**image_file**）  
  
詳しいスクリプトの書き方などの説明はこちら。↓  
https://khufrudamonotes.com/pdf-to-image-python  
  
---
  
「pdf2image」ライブラリが必要です。  
  
```python  
$ pip install pdf2image  
```  
  
---
  
**【pdf_to_PNG_or_dpi150.py】**  
**pdf_file**内にあるpdfを、dpi=150のpngかjpegに（選択して）変換するスクリプト。  
  
**【pdf_to_PNG_dpi150.py】**  
**pdf_file**内にあるpdfを、dpi=150のpngに変換するスクリプト。
  
**【pdf_to_PNG_or_JPEG_dpi150_last_page=1.py】**  
**pdf_file**内にあるpdfの1枚目だけを、dpi=150のpngかjpegに（選択して）変換するスクリプト。  
  
**【pdf_to_PNG_or_JPEG_dpi350.py】**  
**pdf_file**内にあるpdfを、dpi=350のpngかjpegに（選択して）変換するスクリプト。  