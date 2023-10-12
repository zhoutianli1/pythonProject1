import pandas as pd
#建议用jupyter
# 1、获取数据集
facebook = pd.read_csv("D:/周/b站机器学习/数据集/KNN算法预测facebook签到位置/train.csv")

# 2.基本数据处理
# 2.1 缩小数据范围-原数据2000w条太大
facebook_data = facebook.query("x>2.0 and x<2.5 and y>2.0 and y<2.5") #and 或者 &
print(facebook_data)
# 2.2 选择时间特征-将时间戳(秒)转化为python时间格式 https://blog.csdn.net/xuzhexing/article/details/97500039
time = pd.to_datetime(facebook_data["time"], unit="s")
time = pd.DatetimeIndex(time)
facebook_data["day"] = time.day
facebook_data["hour"] = time.hour
facebook_data["weekday"] = time.weekday
# 2.3 去掉签到较少的地方-根据place_id打卡地点分组求 次数，去掉打卡次数少的地点
place_count = facebook_data.groupby("place_id").count()
place_count = place_count[place_count["row_id"]>3]
facebook_data = facebook_data[facebook_data["place_id"].isin(place_count.index)]
# 2.4 确定特征值和目标值
x = facebook_data[["x", "y", "accuracy", "day", "hour", "weekday"]]
y = facebook_data["place_id"]
# 2.5 分割数据集
from sklearn.model_selection import train_test_split, GridSearchCV
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)
# 3.特征工程--特征预处理(标准化)
# 3.1 实例化一个转换器
from sklearn.preprocessing import StandardScaler
transfer = StandardScaler()
# 3.2 调用fit_transform
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)
# 4.机器学习--knn+cv
# 4.1 实例化一个knn估计器
from sklearn.neighbors import KNeighborsClassifier##KNN算法包
estimator = KNeighborsClassifier()
# 4.2 调用gridsearchCV-交叉验证，网格搜索
param_grid = {"n_neighbors": [1, 3, 5, 7, 9]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5, n_jobs=-1)# n_jobs就是用几个cpu跑
# 4.3 模型训练
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
