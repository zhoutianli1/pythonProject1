'''
决策树：
优点：
简单的理解和解释，树木可视化。
缺点：
决策树学习者可以创建不能很好地推广数据的过于复杂的树,容易发生过拟合。

改进：
减枝cart算法
随机森林（集成学习的一种）

多棵“决策树”组成了一片“森林”，计算时由每棵树投票或取均值的方式来决定最终结果，体现了三个臭皮匠顶个诸葛亮的中国传统民间智慧。
决策树的集成思想

'''

'''
集成学习通过建立几个模型来解决单一预测问题。它的工作原理是生成多个分类器/模型，各自独立地学习和作出预测。
这些预测最后结合成组合预测，因此优于任何一个单分类的做出预测

通过训练多个模型，最后结果是 多个模型预测结果的众数
在机器学习中，随机森林是一个包含多个决策树的分类器，并且其输出的类别是由个别树输出的类别的众数而定。

随机森林构造过程中的关键步骤（M表示特征数目）：训练集随机、特征随机

​ 1）每一棵树（模型）的样本：将样本A分为n个小样本ai，一次随机选出一个样本，有放回的抽样，重复n次（有可能出现重复的样本）

​ 2）每一棵树（模型）的特征：样本A有m个特征，随机去选出m个特征, m <<M，建立决策树----只取少量特征，起到降维效果


api：
    sklearn.ensemble.RandomForestClassifier(n_estimators=10, criterion=’gini’, max_depth=None, bootstrap=True, random_state=None, min_samples_split=2)
        n_estimators：integer，optional（default = 10）森林里的树木数量120,200,300,..---可以做交叉验证
        Criterion：string，可选（default =“gini”）分割特征的测量方法--信息真溢 ，可用之前的 信息熵
        max_depth：integer或None，可选（默认=无）树的最大深度 5,8,15,25,30
        max_features="auto”,每个决策树的最大特征数量m
            If “auto”, then max_features=sqrt(n_features).
            If “sqrt”, then max_features=sqrt(n_features)(same as “auto”).
            If “log2”, then max_features=log2(n_features).
            If None, then max_features=n_features.
        bootstrap：boolean，optional（default = True）是否在构建树的样本时使用放回抽样
        min_samples_split:节点划分最少样本数
        min_samples_leaf:叶子节点的最小样本数
        
        
做了哪些改进：
    重构多组样本、特征
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction import DictVectorizer

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

# 3随机森林去进行预测
#3.0随机森林 预估器
from sklearn.ensemble import RandomForestClassifier
estimator = RandomForestClassifier()

#3.1可增加网格搜索、交叉验证
param = {"n_estimators": [120,200,300,500,800,1200], "max_depth": [5, 8, 15, 25, 30]}
# 使用GridSearchCV进行网格搜索
estimator = GridSearchCV(estimator, param_grid=param, cv=3) # cv：指定几折交叉验证，将训练集分成三份，每次取1个作为验证集，这里一共跑6*5*3次

#3.3训练模型
estimator.fit(x_train, y_train)

# 5.模型评估
# 5.1 基本评估方式
score = estimator.score(x_test, y_test)
print("最后预测的准确率为:\n", score)

y_predict = estimator.predict(x_test)
print("最后的预测值为:\n", y_predict)
print("预测值和真实值的对比情况:\n", y_predict == y_test)

# 5.2 使用交叉验证后的评估方式
print("在交叉验证中验证的最好结果:\n", estimator.best_score_)
print("最好的参数模型:\n", estimator.best_estimator_)
print("每次交叉验证后的验证集准确率结果和训练集准确率结果:\n",estimator.cv_results_)

