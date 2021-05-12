#reports the rep name if it has pencil as a item outputs there order in the list

import pandas as pd
import numpy as np

excelfiles = ['/Users/logan/Desktop/SampleData.xlsx','/Users/logan/Desktop/SampleData2.xlsx']


for file in excelfiles:
    df = pd.read_excel(file)
    pencil = df['Rep'].where(df['Item'] == 'Pencil').dropna()
    print(file)
    print(pencil)