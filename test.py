import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

if __name__ == "__main__":
    img = Image.open("./testImage.png")
    print(pytesseract.image_to_string(img))

