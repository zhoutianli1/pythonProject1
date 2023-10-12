'''

交叉验证，网格搜索（模型选择与调优）
将拿到的训练数据，分为训练和验证集。
    将数据分成A、B、C、D 4份，
    每次选其中一份作为验证集。剩下3份作为测试集
    然后经过4次(组)的测试，每次都更换不同的验证集。
    即得到4组模型的结果，取平均值作为最终结果。又称4折交叉验证。

什么是网格搜索(Grid Search)
通常情况下，有很多参数是需要手动指定的（如k-近邻算法中的K值），这种叫超参数。但是手动过程繁杂，所以需要对模型预设几种超参数组合。每组超参数都采用交叉验证来进行评估。最后选出最优参数组合建立模型。
'''

'''
sklearn.model_selection.GridSearchCV(estimator, param_grid=None,cv=None)
    estimator：估计器对象
    param_grid：估计器参数(dict){“n_neighbors”:[1,3,5]}
    cv：指定几折交叉验证,将数据分成A、B、C、D ....n份，
使用，它也是继承于预估器
    .fit：输入训练数据
    .score：准确率
    
    bestscore__:在交叉验证中验证的最好结果
    bestestimator：最好的参数模型
    cvresults:每次交叉验证后的验证集准确率结果和训练集准确率结果
'''

'''
调用 gridsearchCV-交叉验证，网格搜索位置
    在实例化预估器之后
'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 1、获取数据集
iris = load_iris()
# 2、数据基本处理 -- 划分数据集
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
# 3、特征工程：标准化
# 实例化一个转换器类
transfer = StandardScaler()
# 调用fit_transform
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)
# 4、KNN预估器流程
#  4.1 实例化预估器类
estimator = KNeighborsClassifier()
# 4.2 模型选择与调优——网格搜索和交叉验证
# 准备要调的knn的超参数：几组k值
param_dict = {"n_neighbors": [1, 3, 5]}
estimator = GridSearchCV(estimator, param_grid=param_dict, cv=3)
# 4.3 fit数据进行训练
estimator.fit(x_train, y_train)
'''
原来流程knn
estimator = KNeighborsClassifier(n_neighbors=5)#设置邻居数K，实例化预估器类
estimator.fit(X_train, Y_train)#训练 （基于训练集的） 模型
'''
# 5、评估模型效果
# 方法a：比对预测结果和真实值
y_predict = estimator.predict(x_test)
print("比对预测结果和真实值：\n", y_predict == y_test)
# 方法b：直接计算准确率
score = estimator.score(x_test, y_test)
print("直接计算准确率：\n", score)


print("在交叉验证中验证的最好结果：\n", estimator.best_score_)
print("最好的参数模型：\n", estimator.best_estimator_)
print("每次交叉验证后的准确率结果：\n", estimator.cv_results_)
