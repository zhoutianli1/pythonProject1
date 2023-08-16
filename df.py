import pandas as pd

data_file = 'd:/成交明细.xlsx' # Excel文件存储位置
D = pd.read_excel(data_file)

D.to_excel('d:/2.xlsx', sheet_name='Sheet1', index=False,header=True,encoding='utf-8')
print(D)
