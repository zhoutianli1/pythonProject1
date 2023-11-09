import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from time import time
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

#1获取数据集
#data为我们所采用的的数据,review为用户评论数据,label为标签,label=1表示好评,label=0表示差评
t = time()
data = pd.read_csv(r"/home/kesci/input/waimai8451/waimai_10k.csv")
review=data['review'].values
label=data['label'].values

#1.1 把数据分成训练数据集和测试数据集,80%作为训练集,20%作为测试集
Xtrain, Xtest, Ytrain, Ytest = train_test_split(review, label, test_size=0.20, random_state=2)


t1=Xtrain.tolist()
t2=Ytrain.tolist()
news_train = {'review':t1, 'label': np.array(t2)}

#特征工程
vectorizer = TfidfVectorizer(encoding='latin-1')
X_train = vectorizer.fit_transform((d for d in news_train["review"]))
print("n_samples: %d, n_features: %d" % X_train.shape)
print("done in {0} seconds".format(time() - t))

#3模型训练
#直接使用MultinomialNB对数据集进行训练
clf = MultinomialNB(alpha=0.1)

y_train = news_train["label"]
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)


#4测试数据集
#用一条评论来预测其是否准确。
#测试数据集共有2398条数据
print("loading test dataset ...")
t = time()
t11=Xtest.tolist()
t22=Ytest.tolist()
news_test = {'review':t11, 'label': np.array(t22)}
print("summary: {0} documents in 2 categories.".format(
    len(news_test['review'])))
print("done in {0} seconds".format(time() - t))