from sklearn.datasets import load_iris
'''
机器学习开发流程
获取数据  数据处理 
特征工程 
机器学习算法训练模型
模型评估
应用

'''
'''
python机器学习 train_test_split()函数用法解析及示例 划分训练集和测试集 以鸢尾数据为例 入门级讲解:
    https://blog.csdn.net/weixin_48964486/article/details/122866347
鸢尾花数据集：
    输入4个特征（花萼长、宽；花瓣长、宽）值判断属于 3个中的哪一个品种
    包含150个样本 a1~a50、b1~b50、c1~c50
    3个种类，各50个的鸢尾花
    api:
        返回数据格式：.datasets.base.bunch-继承于字典
            sklearn.datasets.load_*、
                小数据集自带在包里面，不用从网上下载，直接加载
            sklearn.datasets.fetch_*(data_home=none,subset)
                大数据集：使用时会先自动从网上下载，
                data_home：从网上下载的数据集保存在电脑中的位置，默认在c盘“用户” 下
                subset:"train" 或者 "test","all",可选，选择要加载的数据集。 训练集的"训练",测试集的"测试",两者的"全部"
    可以通过 .xxx 或者 字典的key-value方式取 值
'''

iris=load_iris()

print("数据集：\n",iris)
print("特征（4个维度）：\n",iris['data'])
print("特征的名字：\n",iris.feature_names)

print("目标值（三个品种）：\n",iris['target'])
print("目标值的名字：\n",iris.target_names)

print("鸢尾花的描述：\n",iris.DESCR)

'''
-------------------------
数据集划分：
    训练集
    测试集
    划分比例：7：3
    train_test_split
    返回数据格式：ndarray
    
    random_state：是随机数的种子。
    设置随机种子在深度学习和数据科学中非常重要，它的主要目的是确保实验的可重复性。 随机性在很多机器学习和深度学习算法中扮演着关键角色，例如在模型初始化、
    数据采样、权重更新等方面都会使用随机数。 如果不设置随机种子，每次运行相同的代码都会产生不同的随机结果，这会使得实验结果难以复现，增加了调试和比较不同模型效果的难度。
'''
#划分数据集：
from sklearn.model_selection import train_test_split
#x:代表特征值 ；y：目标值
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.25,random_state=21)
print("训练集特征x:\n",x_train,'训练集目标y:\n',y_train)
print("测试集train:\n",x_test,'测试集test:\n',y_test)
print('\n训练集大小：',x_train.shape)






