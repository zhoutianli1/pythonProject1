'''
高效的决策，根据将特征排序
决策树：
    先看哪个特征，后看哪个特征，并且可以高效率的分类
    例如：人(年龄、有工作、有房、负债情况）--->是否贷款
        根据哪个顺序来筛选最高效：例如先看有房，则贷款；若没有房有没有工作。有工作贷款，没有工作看负债情况
        本质就是 if-else，像一颗树

    本质就是利用数学方法：自动找到决策顺序

'''

'''
系统越有序，熵值越低；系统越混乱或者分散，熵值越高
信息熵：衡量 信息的量（不确定程度）。熵越小，信息量越小，各种可能性越小，越明确。
信息增益 = entroy(前) - entroy(后)
    衡量使用当前特征对于样本集合D划分效果的好坏。
    根据这个值来排序
    
适用范围：
应用决策树决策方法必须具备以下条件：

（1）具有决策者期望达到的明确目标

（2）存在决策者可以选择的两个以上的可行的备选方案

（3）存在决策者无法控制的两个以上不确定因素

（4）不同方案在不同因素下的收益或损失可以计算出来

（5）决策者可以估计不确定因素发生的概率
'''

'''
api
DecisionTreeClassifier() 模型方法中也包含非常多的参数值。例如：

criterion = gini/entropy 可以用来选择用基尼指数或者熵来做“损失函数”。
splitter = best/random 用来确定每个节点的分裂策略。支持 “最佳” 或者“随机”。
max_depth = int 用来控制决策树的最大深度，防止模型出现过拟合。
min_samples_leaf = int 用来设置叶节点上的最少样本数量，用于对树进行修剪。

原文链接：https://blog.csdn.net/YanqiangWang/article/details/113684621
'''
'''
案例：泰坦尼克号乘客生存预测:
    (根据特征)-----> 预测乘客是否生存
    特征包括票的类别，是否存活，乘坐班次，年龄，登陆home.dest，房间，船和性别等。
    
    当特征包括很多类别：在2特征抽取中：
                         当数据中代表类别的字段较多，先转化为字典--->然后用DictVectorizer对 “字典类型”的数据进行特征抽取
                         或者数据本身是字典
                         将代表类型的city字符串转化为 one-hot编码 ，数值保留
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
# 1、获取数据
titan = pd.read_csv("D:/周/b站机器学习/数据集/泰坦尼克号案例-决策树/train.csv") # 数据我从官网下载下来了
print(titan)
#2.1 确定特征值,目标值
x = titan[:][["Pclass", "Age", "Sex"]] # 票价格 、年龄 、性别 可能对存活率有影响
y = titan[:]["Survived"]
print('取特征：',x)
print('取目的：',y)

# 2.2缺失值需要处理，age中存在大量 空值，进行填补
x['Age'].fillna(x['Age'].mean(), inplace=True)

# 对于x转换成字典数据
x=x.to_dict(orient="records")
print("字典数据x“===============\n",x)

#2.3 划分数据集
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)
print("x_train:---------------------------\n",x_train)

#2.4特征工程：字典类型的特征抽取
transfer = DictVectorizer(sparse=False)
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)
# 查看字典特征提取后的结果；数值-Pclass、Age保留、文章类型特征sex（男、女）转为one-hot)。一共有1+1+2 个新特征
print("查看字典特征提取后的结果:\n",x_train)


# 4.机器学习(决策树)
estimator = DecisionTreeClassifier(criterion="entropy", max_depth=5)
estimator.fit(x_train, y_train)

# 5.模型评估
# 直接对比真实值、预测值
y_predict = estimator.predict(x_test)
print("最后的预测值为:\n", y_predict)
print("预测值和真实值的对比情况:\n", y_predict == y_test)

#计算准确率
score = estimator.score(x_test, y_test)
print("最后预测的准确率为:\n", score)

estimator.predict(x_test)


'''
、决策树可视化
保存树的结构到dot文件
sklearn.tree.export_graphviz() 该函数能够导出DOT格式
tree.export_graphviz(estimator,out_file='tree.dot’,feature_names=[‘’,’’])

'''
from sklearn.tree import export_graphviz

export_graphviz(estimator, out_file="D:/周/b站机器学习/数据集/泰坦尼克号案例-决策树/tree.dot", feature_names=['Age', 'Aclass',  '女性', '男性']) #对应前面新构建的4个特征
