'''
上市公司基本信息：
    获取数据并保存到excel
    描述：获取上市公司基础信息，单次提取4500条，可以根据交易所分批提取

'''
import pandas as pd
import tushare as ts
from utils import dataToExcel

ts.set_token('b1d46e5f0ef73141f8586bbec542c5fc3f16fe99e74fee34102263d6')
pro = ts.pro_api()
# tushare返回数据格式： pandas
data1 = pro.df = pro.stock_company(exchange='SZSE', fields='ts_code,employees,chairman,manager,secretary,reg_capital,setup_date,province')
data2 = pro.df = pro.stock_company(exchange='BSE', fields='ts_code,employees,chairman,manager,secretary,reg_capital,setup_date,province')
data3 = pro.df = pro.stock_company(exchange='SSE', fields='ts_code,employees,chairman,manager,secretary,reg_capital,setup_date,province')

#dataToExcel.dataToExcel(data,'D:\data\getdata_company.xlsx')

print('深交所:',data1.shape,'北交所：',data2.shape,'上交所：',data3.shape)

'''
数据合并和连接：
pd.concat()：连接多个DataFrame。
    参数说明:
    objs: series，dataframe或者是panel构成的序列lsit
    axis： 需要合并链接的轴，0是上下连接，1是左右连接
    join：连接的方式 inner，或者outer
    
DataFrame.merge()：根据共同列合并DataFrame。
    on：列名，join用来对齐的那一列的名字，用到这个参数的时候一定要保证左表和右表用来对齐的那一列都有相同的列名。
    left_on：左表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。
    right_on：右表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。
    left_index/ right_index: 如果是True的haunted以index作为对齐的key
    how：数据融合的方法。
    sort：根据dataframe合并的keys按字典顺序排序，默认是，如果置false可以提高表现。

DataFrame.join()：根据索引或列合并DataFrame。
    dataframe内置的join方法是一种快速合并的方法。它默认以index作为对齐的列。

data1.append(data1, ignore_index=True)
    append方法可以将 series 和 字典就够的数据作为dataframe的"新一行"插入。上下合并
    如果遇到两张表的列字段本来就不一样，但又想将两个表合并，其中无效的值用nan来表示。那么可以使用ignore_index来实现。
        ignore_index=True
'''
dataCompany=pd.concat([data1,data2,data3],axis=0)
dataBasic=dataToExcel.readfile('D:\data\getdata.xlsx')
print('上市公司数据：\n',dataCompany)
print('基础信息数据：\n',dataBasic)
'''
2张不同的表进行，根据股票代码，进行左右信息交叉合并，
'''
dataBasic1=dataBasic.set_index('ts_code')
print(dataBasic1)
dataCompany1=dataCompany.set_index('ts_code')
print(dataCompany1)
Data=pd.concat([dataBasic1,dataCompany1],axis=1)
print('合并数据：\n',Data.head(5))
'''
使用DataFrame.merge()，类sql联结
'''
#上市公司基本信息
dataBasic2=dataBasic.loc[:,['ts_code','industry','exchange']]
print('截取基础信息：\n',dataBasic2)
dataBasic2=dataBasic2.set_index('ts_code')
newData=pd.merge(left=dataBasic2,     #左表表名
                 right=dataCompany1,  #右表表名
                 how='left',          #左连接
                 left_on='ts_code',   #左表连接字段
                 right_on='ts_code'   #右表连接字段
                 )
print(newData)
print(newData.shape,dataBasic2.shape,dataCompany1.shape)
print(newData.groupby('industry').count())

lastData=newData.groupby('industry').agg({'employees':'sum','reg_capital':'sum','chairman':'count'})#员工人数、注册资本、企业老板人数
print(lastData)
print('平均每个行业，的一个公司就业人数:\n',(lastData['employees']/lastData['chairman']).sort_values()) #

