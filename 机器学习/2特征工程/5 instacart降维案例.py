import pandas as pd
#探究用户对商品类别的喜好

#商品与订单信息
order_products = pd.read_csv('D:/周/b站机器学习/数据集/instacart降维案例/order_products__prior.csv')
print(order_products)
#商品信息
products = pd.read_csv('D:/周/b站机器学习/数据集/instacart降维案例/products.csv')
print(products)
#用户订单信息
orders = pd.read_csv('D:/周/b站机器学习/数据集/instacart降维案例/orders.csv')
print(orders)
#商品所属物体类别,有134个类别
aisles  = pd.read_csv('D:/周/b站机器学习/数据集/instacart降维案例/aisles.csv')
print(aisles)

tabel1=pd.merge(aisles,products,on=["aisle_id","aisle_id"])
tabel2=pd.merge(tabel1,order_products,on=["product_id","product_id"])
tabel3=pd.merge(tabel2,orders,on=["order_id","order_id"])
tabel3=tabel3[:10000]#取前1w条数据，要不然太卡了
print(tabel3)

#使用交叉表,
table = pd.crosstab(tabel3["user_id"],tabel3["aisle"])
print(table)

#对数据进行PCA降维 减少信息冗余
from sklearn.decomposition import PCA

# 1、实例化PCA, 小数——保留多少信息
transfer = PCA(n_components=0.9)
# 2、调用fit_transform
data1 = transfer.fit_transform(table)

print("保留90%的信息，降维结果为：\n", data1)
