import ocrmypdf

def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, skip_text=True)

#ocrmypdf --skip-text template1.pdf template2.pdf
#https://youtu.be/1qBVT25mYmg?t=394