import pytesseract
from pdf2image import convert_from_path
import glob
from fpdf import FPDF

pdfs = glob.glob(r"temp/inpath/template1.pdf")

def convert(pdfs):
    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 500)

        for pageNum,imgBlob in enumerate(pages):
            text = pytesseract.image_to_string(imgBlob,lang='eng')

            with open(f'{pdf_path[:-4]}_page{pageNum}.txt', 'w') as the_file:
                the_file.write(text)

# save FPDF() class into 
# a variable pdf
pdf = FPDF()   
   
# Add a page
pdf.add_page()
   
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)
  
# open the text file in read mode
f = open("temp/inpath/template1_page0.txt", "r")
  
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
   
# save the pdf with name .pdf
pdf.output("temp/output_pdf/mygfg1.pdf")   