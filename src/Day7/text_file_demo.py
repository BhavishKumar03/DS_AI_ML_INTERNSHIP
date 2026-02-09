file=open("sample.txt","w")
file.write("Hello, this is a file handling example.")
file.close()
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()


with open("sample.txt","r") as file:
    content=file.read()
    print(content)


try:
    with open("text.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the file name.")


import csv
with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

















from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
sheet = wb.active

for row in sheet.iter_rows(values_only=True):
    print(row)