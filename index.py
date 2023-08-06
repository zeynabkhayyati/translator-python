from PIL import Image
import pytesseract
import pathlib
from googletrans import Translator
translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = ""
text2 = ""

for path in pathlib.Path("en").iterdir() :
    text += pytesseract.image_to_string(Image.open(path), lang="eng")
    text2 += str(translator.translate(text , src="en" , dest="fa"))

    with open('index.txt', 'w' , encoding="Utf8") as file:
        file.write(text)