'''
上市公司基本信息：
    获取数据并保存到excel

'''
import tushare as ts
from utils import dataToExcel
ts.set_token('b1d46e5f0ef73141f8586bbec542c5fc3f16fe99e74fee34102263d6')
pro = ts.pro_api()
data = pro.df = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
print(data)  #tushare返回数据格式： pandas
dataToExcel.dataToExcel(data,'D:\data\getdata_company.xlsx')
