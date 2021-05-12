# pandas manipulates excel data in python
import pandas as pd

excelfiles = ['/Users/logan/Desktop/SampleData.xlsx','/Users/logan/Desktop/SampleData2.xlsx']

# data frames are 2d data structures
merge = pd.DataFrame()

for file in excelfiles:
    df = pd.read_excel(file, skiprows = 1)
    merge = merge.append(df, ignore_index= True)

    #merges two files appends to the last row of file1
merge.to_excel("Merged_files.xlsx")
