'''
https://blog.csdn.net/weixin_45901519/article/details/113929171
分类与回归：
    在分类中：model函数：朴素贝叶斯是计算概率，决策树的“信息熵”的计算公式也是概率

    在回归中： 分为 线性回归、逻辑回归
        1.线性回归
        线性回归(Linear regression)是利用回归方程(函数)对一个或多个自变量(特征值)和因变量(目标值)之间关系进行建模的一种分析方式。
        线性关系- model函数：目标值：h(w)=w1x1+w2x2+....+b  ,xi是自变量（特征值），wi、b是系数
        可以用矩阵表示:h(w)=w1x1+w2x2+....b = (x1,x2,....,xn,b)*(w1,w2,....,wn,1)
            写成python矩阵：[]*[]

        单特征与目标值的关系呈直线关系，或者两个特征与目标值呈现平面的关系,更高维度的我们不用自己去想，记住这种关系即可

        非线性关系-线性模型：
            自变量可能是多次的
            h(w)=w1.x1+w2.x2^2+....wn.xn^k+b

        loss函数：（最小2乘法）：
            模型（系数wi、偏置b）是有误差的=真实值-预测值
            如何改变wi、b，使误差不断减小，更新wi、b
            fun_loss()=(h(w)1-y1)^2 +(h(w)2-y2)^2 +。。。+(h(w)n-yn)^2
                ^2是为了值为正

        优化方法-减小loss
            如何去求模型当中的W WW，使得损失最小？（目的是找到最小损失对应的W值）
            线性回归经常使用的两种优化算法：
                1正规方程：直接求出 wi，b，只求一次。缺点：当特征过多过复杂时，求解速度太慢并且得不到结果，适用于数据量小、特征少的样本 。涉及到矩阵求导
                2梯度下降法：首先随机给一组 wi、b，不断迭代更新 。调整学习率、计算损失函数，学习过程，就是梯度下降算法迭代过程
                    迭代公式：w0=w0-某值
                        w1=w1-某值
                        wn=wn-某值
                    例如只有1个特征，对应w1 ，;迭代调整w1 改变loss值-想象为一个向上的抛物线，向切线斜率减少方向改变w1移动，loss变动
                    步长（学习率learning）：向切线斜率减少方向改变w1移动，取多少合适，避免漏掉最小loss

            2.逻辑回归
            将线性问题------>分类问题
            model函数：线性回归函数+Sigmoid函数
            逻辑回归是不直接预测标签值，而是去预测标签为类别1的概率。一般地如果标签为类别1的概率大于0.5，就认为其为类别1，否在为类别2。
            ，逻辑回归就是线性回归再进行了sigmod变换，其值变化到(0,1).
            二分类本身的输出也是0～1的值。一般来说，当输出值大于0.5时，认为是分类1；当输出值小于0.5时，认为是分类0。所以这个输出值本身就可以看作概率


数据量大于10w 用梯度下降较好，通用性强
数据量小：用岭回归、
正规方程：的使用场景很小

'''

'''
线性回归api:
    sklearn.linear_model.LinearRegression(fit_intercept=True) 通过正规方程优化
    参数
        fit_intercept：是否计算偏置
    返回值： 
        LinearRegression.coef_：查看回归系数
        
        LinearRegression.intercept_：查看偏置



    sklearn.linear_model.SGDRegressor(loss="squared_loss", fit_intercept=True, learning_rate ='invscaling', eta0=0.01)  实现了随机梯度下降学习，它支持不同的loss函数和正则化惩罚项来拟合线性回归模型。
    参数：
        loss:损失类型
            loss=”squared_loss”: 普通最小二乘法
            
        fit_intercept：是否计算偏置
        
        learning_rate : string, optional 学习率的算法
            ‘constant’: 
                算法，eta = eta0 ，学习率为常数eta0，默认0.01
            ‘optimal’: 
                算法，eta = 1.0 / (alpha * (t + t0)) [default]
            ‘invscaling’: 默认值
                算法，eta = eta0 / pow(t, power_t) ，默认power_t=0.25
            对于一个常数值的学习率来说，可以使用learning_rate=’constant’ ，并使用eta0来指定学习率。
    返回值： 
        SGDRegressor.coef_：查看回归系数
        
        SGDRegressor.intercept_：查看偏置

'''