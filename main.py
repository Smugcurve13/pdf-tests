from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    # file = open(filepath,'r')
    pdf.add_page()
    filename =Path(filepath).stem
    pdf.set_font(family='Times',style='b',size=20)
    pdf.cell(w=50,h=8,txt=f"{filename.title()}",ln=1)
    
pdf.output('PDFs/output.pdf')
