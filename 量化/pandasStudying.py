'''
numpy是以矩阵为基础的数学计算模块，提供高性能的矩阵运算，数组结构为ndarray。
    首先需要明确数组与列表的区别：数组是一种特殊变量，虽与列表相似，但列表可以存储任意类型的数据，
    数组只能存储一种类型的数据，同时，数组提供了许多方便统计计算的功能（如平均值mean、标准差std等）。


pandas是基于numpy数组构建的，但二者最大的不同是pandas是专门为处理表格和混杂数据设计的，
    比较契合统计分析中的表结构，而numpy更适合处理统一的数值数组数据。
    pandas数组结构有一维Series和二维DataFrame。
    开发者是一个量化金融分析师，为了应对繁杂的财务数据，开发了pandas

    pandas中文网： https://www.pypandas.cn/

。以下是一些Pandas中常用的主要函数和方法：
数据读取与写入：
pd.read_csv()：从CSV文件读取数据。
pd.read_excel()：从Excel文件读取数据。
pd.read_sql()：从SQL数据库读取数据。
DataFrame.to_csv()：将数据保存为CSV文件。
DataFrame.to_excel()：将数据保存为Excel文件。

数据探索和查看：
DataFrame.head()：查看DataFrame的前几行数据。
DataFrame.tail()：查看DataFrame的后几行数据。
DataFrame.info()：显示DataFrame的基本信息。
DataFrame.describe()：生成关于数值列的统计信息。
DataFrame.shape：返回DataFrame的行数和列数。

数据选择和索引：
DataFrame[column_name]：选择单列数据。
DataFrame[[col1, col2]]：选择多列数据。
DataFrame.loc[row_label, col_label]：通过标签选择数据。
DataFrame.iloc[row_index, col_index]：通过整数位置选择数据。

数据过滤和筛选：
DataFrame[condition]：使用条件筛选数据。
DataFrame.query()：使用查询字符串进行筛选。
DataFrame.isin(values)：检查元素是否在指定的值中。

数据处理和转换：
DataFrame.drop()：删除行或列。
DataFrame.fillna(value)：填充缺失值。
DataFrame.replace(old_value, new_value)：替换特定值。
DataFrame.groupby()：分组数据并进行聚合操作。
DataFrame.apply()：应用函数到行或列。

数据排序和排名：
DataFrame.sort_values(by)：按指定列的值进行排序。
Series.rank()：对数据进行排名。

数据合并和连接：
pd.concat()：连接多个DataFrame。
DataFrame.merge()：根据共同列合并DataFrame。
DataFrame.join()：根据索引或列合并DataFrame。

数据统计和聚合：
Series.mean()：计算平均值。
Series.sum()：计算总和。
Series.min()：找到最小值。
Series.max()：找到最大值。
DataFrame.groupby().agg()：进行自定义聚合操作。

数据可视化：
DataFrame.plot()：生成简单的数据可视化图表。
DataFrame.hist()：绘制直方图。
DataFrame.plot.scatter()：绘制散点图。
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

