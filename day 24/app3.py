from fpdf import FPDF
import pandas

df=pandas.read_csv("data.csv")
pdf=FPDF(orientation="p",format="A4")

for index, item in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=13)
    pdf.set_text_color(100,0,0)
    pdf.set_title(title="python")
    pdf.cell(w=0,h=14,txt=item["Topic"],align="L",ln=1)
    pdf.line(10,22,200,22)
    for i in range(item["Pages"]-1):
        pdf.add_page()

pdf.output("niranjan.pdf")