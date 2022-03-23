import img2pdf

pdf_bytes = img2pdf.convert("temp/inpath/template1_0.png")

file = open("temp/image_path/file2.pdf", "w+b")

file.write(pdf_bytes)

file.close