'''
在 "获取数据的例子.py"中已经获取到了 沪深股票基本信息，并且存到了 getdata.xlsx
获取老八股 和 老五股
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

'''
counts():
    
value_counts(values,sort=True, ascending=False, normalize=False,bins=None,dropna=True)
    作用：根据列名：分组计数，类似group by +count()
    values：“列名”
    sort=True： 是否要进行排序；默认进行排序
    ascending=False： 默认降序排列；
    normalize=False： 是否要对计算结果进行标准化并显示标准化后的结果，默认是False。
    bins=None： 可以自定义分组区间，默认是否；
    dropna=True：是否删除缺失值nan，默认删除
'''
#获取 、交易所数量：value_counts()
print("交易所：\n",data.loc[:,'交易所'].value_counts())

#根据上市日期升序排序  sort_values ,--注不会改变data
print("根据上市日期升序排序:\n",data.sort_values(by=['上市日期'],ascending=False))

#获取中国最早上市的  （沪深市场的）前13个股票
print('前13:\n',data.sort_values('上市日期').head(8+5).loc[:,'股票代码']) #前n，head();后n,tail()

#获取中国最早上市的  上海老八股 和深圳老五股：
'''
条件切片：

'''
# 思路：取深圳市场的上市时间前五的股票，上海市场的上市时间前5的股票
data_sse=data.loc[data['交易所']=='SSE',:]
print('shape:\n',data_sse.shape)
data_sse.index=range(data_sse.shape[0])
data_szse=data.loc[data['交易所']=='SZSE',:]
print("获取交易所为上交所的股票:\n",data_sse.sort_values('上市日期').head(8).loc[:,'股票代码'])
print("获取交易所为深交所的股票:\n",data_szse.sort_values('上市日期').head(5).loc[:,'股票代码'])



'''
apply() 函数的自由度较高，可以直接对 Series 或者 DataFrame 中元素进行逐元素遍历操作，
通常放入一个 lambda 函数表达式、或一个函数作为操作运算，官方上给出的 apply() 用法：

ataFrame.apply(self, func, axis=0, raw=False, result_type=None, args=(), **kwds
func 代表的是传入的函数或 lambda 表达式；
axis 参数可提供的有两个，该参数默认为0/列
    0 或者 index ，表示函数处理的是每一列；
    1 或 columns ，表示处理的是每一行;

raw ；bool 类型，默认为 False;
    False ，表示把每一行或列作为 Series 传入函数中；
    True，表示接受的是 ndarray 数据类型；
    
https://zhuanlan.zhihu.com/p/340770847
'''

print("利用apply遍历：\n",data[data['股票代码'].apply(lambda x:x in [1,600653])])