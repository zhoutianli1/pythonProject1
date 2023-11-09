'''
波士顿房价预测
回归性能评估
    就是 小2乘法 求平均  ，真实值zi，预测值yi：均方误差 = (y1-z1)^2 + (y2-Z2)^2 +......+(ym-zm)^2  / m

'''

def fun1():
    """
    正规方程优化方法：
    api:
    sklearn.linear_model.LinearRegression(fit_intercept=True) 通过正规方程优化
    参数
        fit_intercept：是否计算偏置
    返回值：
        LinearRegression.coef_：查看回归系数

        LinearRegression.intercept_：查看偏置
    :return: 
    """

    #1.获取数据
    import pandas as pd
    titan = pd.read_csv("D:/周/b站机器学习/数据集/波士顿房价预测/boston.csv")  # 数据我从官网下载下来了
    print(titan)
    x = titan["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PIRATIO", "B", "LSTAT"]
    y = titan["MEDV"]
    #2.划分数据集
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=22, test_size=0.2)

    #3.特征工程标准化
    # --考虑 公式为 h(w)=w1x1+w2x2+.....，防止某一类特征值过大
    from sklearn.preprocessing import  StandardScaler
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_test)
    x_test=transfer.transform(x_test)

    #4 构建预估器，并训练模型
    from sklearn.linear_model import  LinearRegression
    estimator = LinearRegression(fit_intercept=True)
    estimator.fit(x_train,y_train)

    #5.查看 wi ,与 b
    print("正规方程wi:\n",estimator.coef_)
    print("正规方程b:\n",estimator.intercept_)

    #均方误差 模型评估
    from sklearn.metrics import mean_squared_error
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test,y_predict)
    print("误差1：",error)
    return None

def fun2():

    """
    梯度下降优化--SGD
        其他方法：SAG、GD
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

    :return:
    """
    # 1.获取数据
    # 特征："CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PIRATIO","B","LSTAT"
    # 目标值：MEDV
    import pandas as pd
    titan = pd.read_csv("D:/周/b站机器学习/数据集/波士顿房价预测/boston.csv")  # 数据我从官网下载下来了
    print(titan)
    x=titan[["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PIRATIO","B","LSTAT"]]
    print(x)
    y=titan[["MEDV"]]
    print(y)
    # 2.划分数据集
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22, test_size=0.2)

    # 3.特征工程标准化
    # --考虑 公式为 h(w)=w1x1+w2x2+.....，防止某一类特征值过大
    from sklearn.preprocessing import StandardScaler
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_test)
    x_test = transfer.transform(x_test)

    # 4 构建预估器，并训练模型
    from sklearn.linear_model import SGDRegressor
    estimator = SGDRegressor(fit_intercept=True,eta0=0.001,max_iter=100) #max_iter迭代次数
    estimator.fit(x_train, y_train)

    # 5.查看 wi ,与 b
    print("梯度下降wi:\n", estimator.coef_)
    print("梯度下降b:\n", estimator.intercept_)

    # 均方误差 模型评估
    from sklearn.metrics import mean_squared_error
    y_predict = estimator.predict(x_test)
    error = mean_squared_error(y_test, y_predict)
    print("误差2：", error)
    return None


if __name__ == "__main__":
    fun2()