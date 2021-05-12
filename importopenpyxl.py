# takes data from two seperate xlsx files then gets data from cell G11


import openpyxl

excelfiles = ['/Users/logan/Desktop/SampleData.xlsx','/Users/logan/Desktop/SampleData2.xlsx']

values = []
for file in excelfiles:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['SalesOrders']
    cell_value = worksheet['G11'].value
    values.append(cell_value)

    print(cell_value)