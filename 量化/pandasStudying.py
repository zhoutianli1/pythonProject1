'''
numpy是以矩阵为基础的数学计算模块，提供高性能的矩阵运算，数组结构为ndarray。
    首先需要明确数组与列表的区别：数组是一种特殊变量，虽与列表相似，但列表可以存储任意类型的数据，
    数组只能存储一种类型的数据，同时，数组提供了许多方便统计计算的功能（如平均值mean、标准差std等）。


pandas是基于numpy数组构建的，但二者最大的不同是pandas是专门为处理表格和混杂数据设计的，
    比较契合统计分析中的表结构，而numpy更适合处理统一的数值数组数据。
    pandas数组结构有一维Series和二维DataFrame。
    开发者是一个量化金融分析师，为了应对繁杂的财务数据，开发了pandas

    pandas中文网： https://www.pypandas.cn/
'''
#-- coding: utf-8 --
import pandas as pd
from utils import dataToExcel


#二维表格数据 DataFrame:
#df=dataToExcel.readfile("D:\data\getdata.xlsx")

df=pd.DataFrame(data=[[1,2,3],[4,5,6]],index=['一','二'],columns=['a','b','c'])
print(df)
print('df行下标index:',df.index)
print('df列下标columns:',df.columns)
print('df值:\n',df.values)

#获取某几行所有数据行：使用切片-

print('行数据\n',df[0:1])

#获取某几列所有数据：使用列下标
print('列数据：\n',df['a'])
print('多列数据:\n',df[['a','b']])

#获取某行某列数据：使用[][]联合
print('取某行某列数据：\n',df[0:1][['a','b']])
print("取某行某列数据loc：\n",df.loc[['一'],['a','c']]) #iloc 行列都索引
print("取某行某列数据loc：\n",df.loc[:,['a','c']]) #iloc 行列都索引
print("取某行某列数据iloc：\n",df.iloc[0:2,1:2])   #iloc 行列都切片

# 打印头部数据，仅查看数据示例时常用
print(df.head())
# 打印列标题
print(df.columns)
# 打印行
print(df.index)
# 打印指定列
# print(df["name"])
# 描述数据
print(df.describe())




#一维数据 Series:
s=pd.Series(data=[1,2,3],index=[11,22,33])
print('一维数据s:\n',s)
print('s行下标index:',s.index)
print('s值:',s.values)

#获取二维df的第一行或者第一列数据--->一维series  ???
s1=df[0:1]
print('s1:\n',s1.values)
s2=df['a']
print('s2:\n',s2.values)


print('pandas基础方法------------------------------------------------------------------------------------------')

