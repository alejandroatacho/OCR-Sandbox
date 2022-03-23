import pytesseract
from PIL import Image
import image2pdf

image_file = "data/template1.jpg"
no_noise = "temp/no_noise.jpg"

img = Image.open(image_file)

ocr_result = pytesseract.image_to_string(img)
"""ocr_result.save(r"temp/pdf_ocr_output.txt")"""
with open('temp/pdf_ocr_output.pdf', 'w') as f:
    f.write(ocr_result)
# print(ocr_result)
