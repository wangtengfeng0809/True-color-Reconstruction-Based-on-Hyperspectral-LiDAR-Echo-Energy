import GBDT as xgb
from GBDT import plot_importance
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
np.set_printoptions(suppress=True)

#1. load dataset
from pandas import read_csv
dataset = read_csv('1270.csv')
values = dataset.values
from sklearn.model_selection  import train_test_split
from sklearn.metrics import mean_squared_error

parameters = {'n_estimators': range(10, 300, 10),
              'max_depth': range(2, 10, 1),
              'learning_rate': [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.3],
              'min_child_weight': range(5, 21, 1),
              'subsample': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
              'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
              'colsample_bytree': [0.5, 0.6, 0.7, 0.8, 0.9, 1],
              'colsample_bylevel': [0.5, 0.6, 0.7, 0.8, 0.9, 1]
              }

#2.tranform data to [0,1]  3个属性，第4个是待预测量
from sklearn.preprocessing import MinMaxScaler
scaler= MinMaxScaler(feature_range=(0, 1))
XY= scaler.fit_transform(values)
#print(XY)

#前28个属性值
#此处每预测出一个值就将该值作为以知量，预测下一个Y值
Featurenum = 30
X = XY[:,0:29]
Y = XY[:,29:30]
print ("样本数据量:%d, 特征个数：%d" % X.shape)
print ("target样本数据量:%d" % Y[0].shape)
#3.split into train and test sets 120个训练集，剩下的都是验证集
#print(len(X),len(X[0]))
#print(Y)
trainX = X[0:1268, :]
trainY = Y[0:1268]
print(trainX)
print(trainY)
#validX = X[n_train_hours1:n_train_hours2, :]
#validY = Y[n_train_hours1:n_train_hours2]
testX = X[1268:2539, :]
testY = Y[1268:2539]

#3构建、拟合、预测
model = xgb.XGBRegressor(max_depth=10, learning_rate=0.01, n_estimators=1000, silent=True, objective='reg:gamma')
model.fit(trainX, trainY)
#保存模型
model.save_model('xgb.model')
#加载模型
bst2 = xgb.Booster()
bst2.load_model('xgb.model')
#模型预测
forecasttestY0 = model.predict(testX)
print('ture = ',values[269:539,29:30])
print('preV = ',forecasttestY0)
write = pd.DataFrame(forecasttestY0)
writer = pd.ExcelWriter('1.xls')
write.to_csv('1.csv')

#4反变换
from pandas import concat
#inv_yhat =np.concatenate((testX,forecasttestY0), axis=1)
#inv_y = scaler.inverse_transform(inv_yhat)
#forecasttestY = inv_y[:,Featurenum]