'''
https://zhuanlan.zhihu.com/p/143092725
思想：根据你的邻居判断类别，通过计算测试数据和已知数据之间的距离来进行分类.
     如果样本xi 与 最近k个样本属于同一类A，那么xi的类别也是A
第一，确定距离度量；
    常用欧式距离，如A(a1,a2,a3) B(b1,b2,b3)
    根号下(a1-b1)^2+(a2-b2)^2+(a3-b3)^2
第二，k值的选择（找出训练集中与带估计点最靠近的k个实例点）；  ------“model: 输入测试集 ， 在模型中计算训练集中与带估计点最靠近的k个实例点”
    k值过大：容易受到异常值影响
    k值过小：容易受到样本不均衡影响
第三，将距离进行递增排序
    选择距离最小的前K个数据
    确定前K个数据的类别，及其出现频率
    返回前K个数据中频率最高的类别（预测结果）

使用前数据处理：标准化
    因为计算欧式距离，若a1-b1非常大，最后计算出来的距离 与其他特征a2 a3无关

KNN适用范围 适用于数据量“较少”（数据量大的时候，需要大量的计算时间和储存空间） 样本分类均衡的场景（如果样本分类不均衡的时候，则分类较少的样本被误分的概率大，这种情况可增加该类样本的权重）
'''

'''
KNN实现鸢尾花分类：
    获取数据
    数据划分
    特征工程
        标准化（knn-计算距离一般要标准化）
    knn计算模型
    模型评估
    

'''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split#用于模型划分
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier##KNN算法包
import numpy as np

# 载入数据集
iris_dataset = load_iris()
X = iris_dataset['data']#特征
Y = iris_dataset['target']#类别

# 数据划分
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

#特征工程标准化
tran=StandardScaler()
X_train = tran.fit_transform(X_train)
X_test = tran.transform(X_test) #使用训练集的fit结果进行 预测集的 标准化

#训练阶段
knn = KNeighborsClassifier(n_neighbors=5)#设置邻居数K，实例化预估器类
knn.fit(X_train, Y_train)#训练 （基于训练集的） 模型



#测试评估模型
Y_pred=knn.predict(X_test)
print("预测结果：",Y_pred)
print("对比真实值",Y_pred==Y_test)

score =knn.score(X_test,Y_test)
print("准确率：",score*100,"%")


# 做出预测，预测花萼长5cm宽2.9cm，花瓣长1cm宽0.2cm的花型
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print("Prediction:{}".format(prediction))
print("Predicted target name:{}".format(iris_dataset['target_names'][prediction]))
