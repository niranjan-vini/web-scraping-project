from fpdf import FPDF
import pandas

df=pandas.read_csv("data.csv")
pdf=FPDF(orientation="p",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

for index, item in df.iterrows():
    # header in pdf
    #add pages in pdf
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=13)   #select font
    pdf.set_text_color(100,0,0)   #text color red or green or blue
    pdf.cell(w=0,h=14,txt=item["Topic"],align="L",ln=1)    # add text in pdf and required side,break line
    pdf.line(10,22,200,22)  # add text underline

    # add footer
    pdf.ln(260) #break line
    pdf.set_font(family="Times", style="B", size=9)  # select font
    pdf.set_text_color(1, 100, 0)
    pdf.cell(w=0, h=14, txt=item["Topic"], align="R", ln=1)

    for i in range(item["Pages"]-1):
        pdf.add_page()

        #add footere
        pdf.ln(271)
        pdf.set_font(family="Times", style="B", size=9)  # select font
        pdf.set_text_color(1, 100, 0)
        pdf.cell(w=0, h=14, txt=item["Topic"], align="R", ln=1)

pdf.output("niranjan.pdf")