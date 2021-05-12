#appyls formulas across workbooks
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
excelfiles = ['/Users/logan/Desktop/SampleData.xlsx','/Users/logan/Desktop/SampleData2.xlsx']

for file in excelfiles:
    wb = openpyxl.load_workbook(file)
    Worksheet = wb["SalesOrders"]
    Worksheet['G46'] = '=AVERAGE(G3:G45)'
    wb.save(file)