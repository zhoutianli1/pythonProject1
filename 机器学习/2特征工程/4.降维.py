'''
降维：
    拿到样本数据(/样本特征)： n行（样本个数） ；m列(特征个数)
    降维指的是减少特征个数：
        将一组相关特征转化为无关特征，减少信息冗余

    例如鸟（体格大小；羽毛长度；羽毛颜色；是否有爪子）
        显然 是否有爪子 应该过滤；这个特征的方差也小

    降维方法：
Filter(过滤式)：主要探究特征本身特点、特征与特征和目标值之间关联
    方差选择法：低方差特征过滤
    相关系数：特征与特征之间的相关程度 ，取值范围 -1到1

Embedded (嵌入式)：算法自动选择特征（特征与目标值之间的关联）
    决策树:信息熵、信息增益
    正则化：L1、L2
    深度学习：卷积等

    降维目的：
        删除某几列数据（特征），或者
'''



'''
2.3 低方差特征过滤
删除低方差的一些特征，前面讲过方差的意义。再结合方差的大小来考虑这个方式的角度。

    特征方差小：某个特征大多样本的值比较相近
    特征方差大：某个特征很多样本的值都有差别
    
2.3.1 API
    sklearn.feature_selection.VarianceThreshold(threshold = 0.0)
        删除所有"低方差"特征:方差低，说明特征的值几乎都一样，不适合作为特征
        threshold：删除低于它的特征
            
        Variance.fit_transform(X)
        X:传入参数：numpy array格式的数据[n_samples,n_features]，二维数组
        返回值：训练集差异低于threshold的特征将被删除。默认值是保留所有非零方差特征，即删除所有样本中具有相同值的特征。
'''
import pandas as pd
import numpy as np
from sklearn.feature_selection import VarianceThreshold

def variance_demo():
    """
    删除低方差特征——特征选择
    :return: None
    """
    data =data =np.array([[1,2,3,4,],[1,5,6,4],[1,8,9,4]])
    print(data)
    # 1、实例化一个转换器类
    transfer = VarianceThreshold(threshold=0)
    # 2、调用fit_transform
    data = transfer.fit_transform(data)
    print("删除低方差特征的结果：\n", data)
    print("形状：\n", data.shape)

    return None

'''
2.4相关系数：
    当几个特征相关性很高时的处理
        （1）选取其中一个，其余舍弃
        （2）将数个特征合并为一个
        （3）主成分分析
'''

from scipy.stats import pearsonr
def pea_demo():
    """
    皮尔逊相关系数
        返回结果(r,p)
            r是相关系数，处于[-1，1]之间 ，r越接近1，表示相关性越强，  当|r|=1 , y=kx


    :return:
    """
    # 准备数据
    x1 = [12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9]
    x2 = [21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]

    # 判断
    ret = pearsonr(x1, x2)
    print("皮尔逊相关系数的结果是：\n", ret)




from scipy.stats import spearmanr

def spea_demo():
    """
    斯皮尔曼相关系数
        反映变量之间相关关系密切程度的统计指标
        斯皮尔曼相关系数表明 X (自变量) 和 Y (因变量)的相关方向。 如果当X增加时， Y 趋向于增加, 斯皮尔曼相关系数则为正
        与之前的皮尔逊相关系数大小性质一样，取值 [-1, 1]之间

        斯皮尔曼相关系数比皮尔逊相关系数应用更加广泛
    :return:
    """
    # 准备数据
    x1 = [12.5, 15.3, 23.2, 26.4, 33.5, 34.4, 39.4, 45.2, 55.4, 60.9]
    x2 = [21.2, 23.9, 32.9, 34.1, 42.5, 43.2, 49.0, 52.8, 59.4, 63.5]

    # 判断
    ret = spearmanr(x1, x2)
    print("斯皮尔曼相关系数的结果是：\n", ret)






'''
2.5:
主成分分析：
    将数据分解为较低维数空间    
    在降维过程中保存尽量多的信息
'''

from sklearn.decomposition import PCA

def pca_demo():
    """
    对数据进行PCA降维
    https://blog.csdn.net/weixin_45901519/article/details/114867047?spm=1001.2014.3001.5502
    参数：
        n_components: 可以为小数、或者整数
            小数：表示保留百分之多少的信息
            整数：减少到多少特征
    :return: None
    """
    #4维数据
    data = [[2,8,4,5], [6,3,0,8], [5,4,9,1]]

    # 1、实例化PCA, 小数——保留多少信息
    transfer = PCA(n_components=0.9)
    # 2、调用fit_transform
    data1 = transfer.fit_transform(data)

    print("保留90%的信息，降维结果为：\n", data1)

    # 1、实例化PCA, 整数——指定降维到的维数
    transfer2 = PCA(n_components=3)
    # 2、调用fit_transform
    data2 = transfer2.fit_transform(data)
    print("降维到3维的结果：\n", data2)

    return None

if __name__=='__main__':
    pca_demo()