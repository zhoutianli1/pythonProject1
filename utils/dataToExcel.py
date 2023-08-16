
'''
作用：将数据保存到D盘下的excel中
常用的读写Excel的库：

pandas
openpyxl
xlrd/xlwt/xlutils
使用它们都能够达到读写Excel的目的，但它们的侧重点又略有不同。

具体如下：
pandas：数据处理最常用的分析库之一，可以读取各种各样格式的数据文件，一般输出dataframe格式，功能强大
openpyxl：主要针对xlsx格式的excel进行读取和编辑
xlrd库：从excel中读取数据，支持xls、xlsx
xlwt库：对excel进行修改操作，不支持对xlsx格式的修改
Microsoft Excel API：需安装pywin32，直接与Excel进程通信，可以做任何在Excel里可以做的事情，但比较慢
'''
import pandas as pd
#-- coding: utf-8 --

#读文件:
def readfile(file_path):

    df = pd.read_excel(file_path, sheet_name = "Sheet1") # sheet_name不指定时默认返回全表数据


    # 打印头部数据，仅查看数据示例时常用
    print(df.head())

    # 打印列标题
    print(df.columns)

    # 打印行
    print(df.index)

    # 打印指定列
    #print(df["name"])

    # 描述数据
    print(df.describe())
    return df

#写文件:
def dataToExcel(data,load):

    data.to_excel(load)




data= readfile('D:\data\getdata.xlsx')
print(data)