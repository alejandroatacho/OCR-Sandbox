import pytesseract
from PIL import Image
import img2pdf

image_file = "data/template1.jpg"
no_noise = "temp/no_noise.jpg"
pdf_path = "temp/converted_fix_ocr2.pdf"
img = Image.open(image_file)

ocr_result = pytesseract.image_to_string(img)

pdf_bytes = img2pdf.convert(no_noise)

# print(ocr_result)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
img.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
