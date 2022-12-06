import pdfplumber
import re

with pdfplumber.open(r"F:\sequelstring\pdf\drugs_extract.pdf") as pdf:
    pages = pdf.pages
    # print(pages)
    text1 = " "

    for page in pages:
        text = page.extract_text()
        # print(text)
        text1 += text

po_no = re.search("PO\s\D+\d+\/\D+\d+\/\D+\d+", text1).group()
po_no = re.sub(r"PO No.|\:", " ", po_no).strip()
# print(po_no)

po_date = re.search("PO\s+\D+\d+\/+\d+\/\d+", text1).group()
po_date = re.sub("PO Date.|\:", " ", po_date).strip()  
# print(po_date)

new_line = re.search("(?si)net.*?Rupees", text1).group()
new_line = re.sub("Net|Rupees", " ", new_line).strip()
# print(new_line)

des = re.findall("\d+\s+[A-Z]+\s+[0-9A-Z]+\s+[0-9A-Z]+.*?\n", new_line)
# print(des)

for item in range(len(des)):
    # print(des[item].split())

    new_data = des[item].split()

    Net = new_data[-1]
    # print(Net)

    Others = new_data[-2]
    # print(Others)

    IGST = new_data[-3]
    # print(IGST)

    CGST = new_data[-4]
    # print(CGST)

    SGST = new_data[-5]
    # print(SGST)

    Disc_Amt = new_data[-6]
    # print(Disc_Amt)

    Gross = new_data[-7]
    # print(Gross)

    Rate = new_data[-8]
    # print(Rate)

    Qty_UOM = new_data[-9]
    # print(Qty_UOM)

    MRP = new_data[-10]
    # print(MRP)

    Item = ' '.join(new_data[1:-10])
    # print(Item)

    Sr_No = new_data[0]
    # print(Sr_No)


    list_data =[Sr_No, Item, MRP, Qty_UOM, Rate, Gross, Disc_Amt, SGST, CGST, IGST, Others, Net]
    print(list_data)

















