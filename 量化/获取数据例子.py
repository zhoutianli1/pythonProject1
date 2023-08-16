'''
tushare 的 token ： b1d46e5f0ef73141f8586bbec542c5fc3f16fe99e74fee34102263d6
在Tushare数据接口里，股票代码参数都叫ts_code，每种股票代码都有规范的后缀：
    上海证券交易所	SSE	.SH	600000.SH(股票) 000001.SH(指数)
    深圳证券交易所	SZSE	.SZ	000001.SZ(股票) 399005.SZ(指数)
    北京证券交易所	BSE	.BJ	8和4开头的股票
    香港证券交易所	HKEX	.HK	00001.HK

tushare返回数据格式： pandas的dataframe格式
'''

import tushare as ts
from utils import dataToExcel
ts.set_token('b1d46e5f0ef73141f8586bbec542c5fc3f16fe99e74fee34102263d6')

#初始化pro接口
pro = ts.pro_api()

'''
#利用掉用pro里面的 方法：
stock_basic-股票基本信息
'''


#具体参数作用去看官方文档
#获取的指标名称
fields='ts_code,symbol,name,area,industry,list_date,market,exchange'
data = pro.stock_basic(exchange='', list_status='L', fields=fields)
print(data)  #tushare返回数据格式： pandas
dataToExcel.dataToExcel(data,'D:\data\getdata.xlsx')