'''
上市公司--地域、行业分析

'''

from utils import dataToExcel
data= dataToExcel.readfile('D:\data\getdata.xlsx')
print("-----------------------------------------------------------")
data.columns=['Unnamed','ts股票代码','股票代码','股票名称','地区','所属行业','市场类别（主板/创业板/科创板/CDR/北交所','交易所','上市日期']

'''
1.每个地域有多少上市公司：
    假如用sql，我会考虑使用 select count(*) from data group by '地域'
    pandas中的gooupby函数
'''

print("group by分组：\n",data.groupby('地区').count())
print("group by分组：\n",data.groupby('地区').count().iloc[:,0])

#.describe()
print("对上面数据计算标准差、中位数等：\n",data.groupby('地区').count().iloc[:,0].describe([0.1,0.2,0.3,0.4,0.55,0.6,0.7,0.8]))

'''
pyecharts 地图;
    去下载该包，
    作用：在中国地图上，展示
'''