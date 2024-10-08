from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Text Files/*.txt")

for filepath in filepaths:
    # file = open(filepath,'r')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    for i in range(len(filepaths)+1):
        filename =Path(filepath).stem
        pdf.set_font(family='Times',style='b',size=20)
        pdf.cell(w=8,h=12,txt=f"{filename.title()}")
        pdf.add_page()
        pdf.output('PDFs/output.pdf')

