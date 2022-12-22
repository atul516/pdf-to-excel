import camelot
import PyPDF2
import os
# Open the PDF file in read-binary mode(converts file into binary format) using the open()
# function and store it in a variable.
cwd = os.getcwd()
basepath = cwd
pdfpath = os.path.join(basepath, 'fwd')
os.chdir(pdfpath)
files = os.listdir(os.getcwd())
excel_files = [x for x in files if x.endswith('.pdf')]

for file in excel_files:
    gvn_file = open(file, 'rb')
    pdf_read = PyPDF2.PdfFileReader(gvn_file)
    pages_count = pdf_read.numPages
    for i in range(1,pages_count+1):
        file_name = f"files1/{file.split('.')[0]}_{i}.csv"
        page = f"{i}"
        tables = camelot.read_pdf(file, flavor='stream', edge_tol=500, pages=page)
        tables[0].to_csv(file_name)
