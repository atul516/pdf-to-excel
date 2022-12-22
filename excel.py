import tabula
from tabula import convert_into

src_pdf = r"23.pdf"
des_csv = r"23.csv"
convert_into(src_pdf, des_csv, guess=False, lattice=False, stream=True, pages="all")
# Read PDF File
# this contain a list
#df = tabula.read_pdf("", pages='all')[0]
# Convert into Excel File
