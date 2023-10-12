'''
归一化，标准化（无量纲化）；
特征预处理：通过一些转换函数将特征数据转换成更加适合算法模型的特征数据过程
所有机器学习算法的成功取决于如何呈现数据。” “特征工程是一个看起来不值得在任何论文或者书籍中被探讨的一个主题。但是他却对机器学习的成功与否起着至关重要的作用

意义：特征的单位或者大小相差较大，或者某特征的方差相比其他的特征要大出几个数量级，容易影响（支配）目标结果，使得一些算法无法学习到其它的特征
'''






'''
归一化：假设缩放区间[A:B]
对样本：每一列，x_=(Xi-min)/(max-min)   ;x_i=x_*(B-A)+A

API:
sklearn.preprocessing.MinMaxScaler (feature_range=(0,1)… )
    MinMaxScalar.fit_transform(X)
    X:numpy array格式的数据[n_samples,n_features]
    返回值：转换后的形状相同的array

'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def stand_demo():
    """
    标准化演示
    :return: None
    """
    data =np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(data)
    # 1、实例化一个“转换器类”
    transfer = MinMaxScaler(feature_range=(0,1))
    # 2、调用“fit_transform“
    data = transfer.fit_transform(data)
    print("标准化的结果:\n", data)

    return None


'''
标准化：
    归一化，最大值与最小值非常容易受异常点影响，所以这种方法鲁棒性较差，只适合传统精确小数据场景，
        例如异常值经常为最大、最小值，在这种场景下使用归一化，误差很大
标准化公式：(Xi-本列均值)/本列方差
    方差衡量是离散程度，就算有异常值，在大量样本下也不会有太大影响
'''

from sklearn.preprocessing import StandardScaler

def stand_demo1():
    """
    标准化演示
    :return: None
    """
    data =np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(data)
    # 1、实例化一个转换器类
    transfer = StandardScaler()
    # 2、调用fit_transform
    data = transfer.fit_transform(data)
    print("标准化的结果:\n", data)
    print("每一列特征的平均值：\n", transfer.mean_)
    print("每一列特征的方差：\n", transfer.var_)

    return None

if __name__=='__main__':
    stand_demo1()