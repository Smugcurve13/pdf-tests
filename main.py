from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files/*.txt")
pdf = FPDF(orientation='P', unit='mm', format='A4')

for filepath in filepaths:
    pdf.add_page()

    # Add a title
    filename =Path(filepath).stem
    pdf.set_font(family='Times',style='b',size=20)
    pdf.cell(w=50,h=8,txt=f"{filename.title()}",ln=1)

    # Add body of file
    pdf.set_font(family='Times',size=10)
    with open(filepath,'r') as file:
        pdf.multi_cell(w=180,h=8,txt=file.read())

pdf.output('PDFs/output.pdf')
