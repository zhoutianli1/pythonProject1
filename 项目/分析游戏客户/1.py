'''
游戏业务：用户行为
    下载 安装 激活  注册 登录 充值 消耗
    分析：安装和注册信息
'''


# 加载包
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据-安装信息az 和 注册信息zc
az = pd.read_excel('./数据源整合.xlsx',sheet_name='安装信息')
zc = pd.read_excel('./数据源整合.xlsx',sheet_name='注册信息')

print("\n===安装信息表：")
print(az.info())
print('空值统计:\n',az.isnull().sum())
print('重复数据：',az.duplicated().sum())

print("\n===注册信息表：")
print(zc.info())
print('空值统计:\n',az.isnull().sum())
print('重复数据：',az.duplicated().sum())

print('安装信息表的安装时间范围：',az['安装时间'].min(),az['安装时间'].max())
print('注册信息表的安装时间范围：',zc['安装时间'].min(),zc['安装时间'].max())

#为了方便分析，选择安装时间在 2020-4-20——2020-04-26 的数据
az = az[az['安装时间']>'2020-04-19 23:59:59']
zc = zc[zc['安装时间']>'2020-04-19 23:59:59']

#安装后，完成注册的百分比：选择注册信息表中'用户唯一ID'存在安装表中的数据
uid = az['用户唯一ID']
zc = zc[zc['用户唯一ID'].isin(uid)]


print('注册次数：',zc.shape)
print('注册信息重复ID：',zc['用户唯一ID'].duplicated().sum())
# 去重
zc = zc.drop_duplicates('用户唯一ID')
print('去重后 注册人数：',zc.shape)

'''
安装信息分析

'''
print('安装人数：',az.shape)
print('注册人数：',zc.shape[0])
print('激活率：%.2f%%'%((zc.shape[0]/az.shape[0])*100))

print("\n安装渠道：\n",az['渠道'].value_counts())

az['安装日期']=az['安装时间'].dt.date
print('\n日安装用户量：\n',az.groupby('安装日期').用户唯一ID.count())


'''
注册信息分析
'''
zc['注册日期'] = pd.to_datetime(zc['注册时间']).dt.date
print('日注册用户：\n',zc.groupby('注册日期').用户唯一ID.count())

print("用户新老用户类型：\n",zc['用户类型'].value_counts())

zc['注册时段'] = pd.to_datetime(zc['注册时间']).dt.hour
hzc = zc.groupby(['用户类型','注册时段']).用户唯一ID.count().reset_index(name='total')
sns.lineplot(data=hzc,x='注册时段',y='total',hue='用户类型')
plt.title('各时段的注册用户量',loc='left')
plt.show()

print('日新增新用户：\n')
nzc = zc[zc['用户类型']=='new']
nzc.groupby('注册日期').用户唯一ID.count()