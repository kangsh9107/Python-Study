import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# a = Image.open('영수증.jpg')
# result = pytesseract.image_to_string(a, lang='kor')
a = Image.open('카드3.jpg')
result = pytesseract.image_to_string(a)
print(result)



# 데이터 출력 형식
# str = ""
# for r in result.split():
#     str += r
# print(str)
