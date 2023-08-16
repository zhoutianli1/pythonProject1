'''
在 "获取数据的例子.py"中已经获取到了 沪深股票基本信息，并且存到了 getdata.xlsx

对 沪深股票基本信息 进行处理

exchange	str	N	交易所 SSE上交所 SZSE深交所 BSE北交所
market	str	N	市场类别 （主板/创业板/科创板/CDR/北交所）
'''
import pandas as pd
from utils import dataToExcel

data= dataToExcel.readfile('D:\data\getdata.xlsx')
print("-----------------------------------------------------------")
print('data:\n',data[0:1][:],'列名:\n',data.columns)
print("更换列名：")
#从 excel拿数据后多了一列Unnamed
data.columns=['Unnamed','ts股票代码','股票代码','股票名称','地区','所属行业','市场类别（主板/创业板/科创板/CDR/北交所','交易所','上市日期']

'''
 "  :  " 可以理解为 “到”
 loc中：  ':'左右2边是行列索引名 ，包前包后
 iloc中： ':'左右2边是行列位置名 ，包前不包后
'''
print('loc-data:\n',data.loc[0,:])   #loc中：这里0代表第一行的行索引名称，series数据
print('loc-data:\n',data.loc[[0],:])   #loc中：这里0代表第一行的行索引名称,dataframe数据
print('iloc-data:\n',data.loc[0,:])   #iloc中：这里0代表第一行，series数据
print('iloc-data:\n',data.loc[[0],:])   #iloc中：这里0代表第一行,dataframe数据
print('data数据量：\n',data.shape)


#获取 有哪些交易所： unique()去重
print("交易所：\n",data.loc[:,'交易所'].unique())

#获取 、交易所数量：value_counts()
print("交易所：\n",data.loc[:,'交易所'].value_counts())

#根据上市日期升序排序  sort_values ,--注不会改变data
print("根据上市日期升序排序:\n",data.sort_values(by=['上市日期'],ascending=False))

#获取中国最早上市的  老八股 和老五股
print('老八股 和老五股:\n',data.sort_values('上市日期').head(8+5).loc[:,'股票代码']) #前n，head();后n,tail()
