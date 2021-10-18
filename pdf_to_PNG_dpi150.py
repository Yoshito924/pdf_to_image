import os
from pathlib import Path
from pdf2image import convert_from_path
import glob

# poppler/binを環境変数PATHに追加する
poppler_dir = Path(__file__).parent.absolute() / "poppler/bin"
os.environ["PATH"] += os.pathsep + str(poppler_dir)

# PDFファイルのパスを取得し順番に捌いていく
for x in glob.glob("./pdf_file/*.pdf"):
    pdf_path = Path(x)

    # pdfから画像に変換
    pages = convert_from_path(pdf_path, dpi=150)

    # 画像ファイルを1ページずつ「image_file」に保存する。
    image_dir = Path("./image_file")

    for i, page in enumerate(pages):
        # ファイルネームを決定する。
        file_name = f'{pdf_path.stem}_{i + 1:02}.png'
        image_path = f'{image_dir}/{file_name}'
        # PNGで保存
        page.save(image_path, "PNG")
