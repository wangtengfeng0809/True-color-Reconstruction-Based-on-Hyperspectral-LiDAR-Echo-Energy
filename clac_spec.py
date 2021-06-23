import numpy as np
import scipy.io as scio
import pandas as pd
import xlwt

def sigmoid(X,useStatus,i):
    if useStatus:
        #return 1.0 / (1 + np.exp(-float(X)))
        fenzi = np.exp(i * (X ** 2)) - np.exp(i * (- X ** 2))
        fenmu = np.exp(i * (X ** 2)) + np.exp(i * (- X ** 2))
        return fenzi/fenmu
    else:
        return float(X)

def MaxMinNormalization(x,Max,Min):
    x = (x - Min) / (Max - Min);
    return x;

def Z_ScoreNormalization(x,mu,sigma):
    x = (x - mu) / sigma;
    return x;

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet1")

c = scio.loadmat('./470700.mat')
data = c['num']
npdata = np.array(data)
print(npdata)
rst = []
writer = MaxMinNormalization(npdata,np.max(npdata),np.min(npdata))

resource = scio.loadmat('./470700.mat')
data_r = resource['num']
r_data = np.array(data_r)
init_i = 0

white_spec = 8016.4

for count in range(1000):
    sum = 0
    init_i = init_i + 0.01
    sigmoid_value = sigmoid(writer, 1, init_i)
    for i in range(0, 4):
        for j in range(0, 24):
            sum = sum + (sigmoid_value[i][j] - r_data[i][j])
    mean = sum / 4 / 24
    rst.append(mean)
    print("count = ", count , "init_i = ", init_i, "mean = ", mean)

writeExl = sigmoid(writer, 1, 9.86)

for i in range(0, 24):
    for j in range(0,24):
        worksheet.write(i, j, data[i][j]/white_spec)

#for i in range(1000):
#    worksheet.write(i, 1, rst[i])

workbook.save("white8627.xls")


#print(Z_ScoreNormalization(npdata,npdata.mean(),npdata.std()))
#print(sigmoid(npdata,1))