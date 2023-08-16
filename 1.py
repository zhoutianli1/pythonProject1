import json

import tushare as ts
import pandas as pd

from MyEncoder import MyEncoder

ts.set_token('b1d46e5f0ef73141f8586bbec542c5fc3f16fe99e74fee34102263d6')#设置token，只需设置一次
#api  = ts.pro_api()#初始化接口
#data= api.stock_basic(fields='ts_code,name,list_date')
pro = ts.pro_api()

#多个股票，日线行情数据
df_basic = pro.daily(ts_code='000001.SZ,600000.SH', start_date='20180701', end_date='20180718')

#stock_basic数据,stock_basic()接口获取已上市的所有股票基础信息数据，包括股票代码、名称、上市日期、退市日期、所属板块等。
# df_basic= pro.stock_basic()
# df_basic.to_excel('d:/已上市的所有股票基础信息.xlsx', sheet_name='Sheet1', index=False,header=True,encoding='utf-8')


data_file = 'd:/已上市的所有股票基础信息.xlsx' # Excel文件存储位置
D = pd.read_excel(data_file)
df_basic=D[(D["industry"] == u"水泥")]

#https://blog.csdn.net/qq_46293423/article/details/105785007
#dataframe数据类型-->josn--->存入josn文件
#df_basic = df_basic.to_json()
with open("stock_pool.json", "w", encoding='utf-8') as f:
     json.dump(df_basic, f, ensure_ascii=False, indent=4, cls=MyEncoder)

#使用open()把json文件打开，然后使用load()将文件中JSON编码字符串转换成Python数据类型，比如：
with open("stock_pool.json", 'r') as load_f:
    stock_index = json.load(load_f)
print(stock_index)

#创建数据库的代码：
#conn = sqlite3.connect('stock-boards.db')