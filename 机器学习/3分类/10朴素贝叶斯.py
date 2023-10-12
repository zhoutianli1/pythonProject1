'''
https://blog.csdn.net/qq_43723172/article/details/104828221
P(A|B)是在条件B发生的情况下A发生的概率，P(AB)是条件A与B同时发生的概率。
独立事件即是指两个事件的发生不互相影响
例子： 今天我上街的概率是1/3，不上街的概率是2/3;你上街的概率是2/3，不上街的概率是1/3。则可设A事件为我上街，B事件为你上街，则P(A)=1/3 , P(B)=2/3，也有P(A|B)=P(AB)/P(B)=(1/3 * 2/3)/(2/3)=1/3=P(A)

贝叶斯：
    公式：p(B/A)=p(A/B)*  p(b)/p(A)
'''

'''
朴树贝叶斯：
    A是特征，B是目标
    朴树:特征之间是“相互独立”的 --这是假设
    对缺失数据 不敏感
    分类准确率高、速度快
    当文本词有关联时，准确度受到影响
    
    应用场景：文本分类-词于词之间是相互独立的。朴素贝叶斯算法是一种基于概率论的分类算法，它的分类效率高、准确率高，常用于文本分类、情感分析、垃圾邮件过滤等领域。
    api：
        
'''

'''
案例：20个新闻组分类
    步骤：1获取数据：sklearn自带数据
         2划分数据集
         3特征工程-文本特征抽取 -tf-idf    
         4朴素贝叶斯
         5模型评估
         6调优
'''
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
def news():
    """
    用朴树贝叶斯 对新闻分类
    :return:
    """
    #1
    # subset:"train" 或者 "test","all",可选，选择要加载的数据集。 训练集的"训练",测试集的"测试",两者的"全部"
    #sklearn提供的文本语料为20newsgroups新闻语料，如果让sklearn自己下载语料，基本会失败，所以我们要用手动下载。https://blog.csdn.net/xiaotian127/article/details/86836571
    #默认下载位置 c盘下用户
    news=fetch_20newsgroups(subset="all")

    #2
    x_train,x_test,y_train,y_test=train_test_split(news.data,news.target)

    #3特征工程 tfidf
    transfer = TfidfVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    #4朴树贝叶斯 预估器
    estimator = MultinomialNB()  # alpha：默认值为1，为防止计算出的分类概率为0
    estimator.fit(x_train,y_train)
    # 4.2 调用gridsearchCV-交叉验证，网格搜索
    param_grid = {"alpha": [1, 3, 2]}
    estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5, n_jobs=-1)  # n_jobs就是用几个cpu跑

    # 5.1 基本评估方式
    score = estimator.score(x_test, y_test)
    print("最后预测的准确率为:\n", score)

    y_predict = estimator.predict(x_test)
    print("最后的预测值为:\n", y_predict)
    print("预测值和真实值的对比情况:\n", y_predict == y_test)

    # 5.2 使用交叉验证后的评估方式
    print("在交叉验证中验证的最好结果:\n", estimator.best_score_)
    print("最好的参数模型:\n", estimator.best_estimator_)
    print("每次交叉验证后的验证集准确率结果和训练集准确率结果:\n", estimator.cv_results_)

    return None

if __name__ == "__main__":
    news()