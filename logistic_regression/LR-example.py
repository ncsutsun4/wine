import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

#用0,1去做分類

data = pd.read_csv('testData.csv', header=None)
# print(data)

#計算機率函數
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
    
#計算平均梯度
def gradient(data, w): # 偏微分方向
    g = np.zeros(len(w))
    for index, row in data.iterrows(): # x是訓練資料 y是該筆資料屬於的類別
        x = np.array(row[[0, 1, 2]])
        error = sigmoid(w.T.dot(x))
        g += (error - float(row[[3]])) * x
    return g / len(data)

#計算現在的權重的錯誤有多少
def cost(data, w): # Loss funcion
    total_cost = 0
    for index, row in data.iterrows():
        x = np.array(row[[0, 1, 2]]) # 訓練資料x
        error = sigmoid(w.T.dot(x))
        total_cost += abs(row[[3]] - error)
    return total_cost

def logistic(dataset): #演算法實作

    w = np.zeros(3) #用0 + 0*x1 + 0*x2當作初始設定  (初始設定w為(0, 0, 0))

    limit = 10 # 更新十次後停下

    eta = 1 # 更新幅度

    costs = [] # 紀錄每次更新權重後新的cost是多少

    for i in range(limit):
        current_cost = cost(dataset, w) # 當前訓練iteration的cost
        print('current_cost=' + str(current_cost))
        costs.append(current_cost)
        w = w - eta * gradient(dataset, w)  # w更新的方式: w - learning_rate * 梯度 (例如第一輪，試算出w在w=[0 0 0]時對L的偏微結果)
        eta *= 0.95 # Learning Rate，逐步遞減

    #畫出cost的變化曲線，他應該要是不斷遞減 才是正確

    plt.plot(range(limit), costs)
    plt.show()
    return w
# #執行


w = logistic(data)
#畫圖
print(w)

# ps = [v[0] for v in dataset]
# fig = plt.figure()
# ax1 = fig.add_subplot(111)

# ax1.scatter([v[1] for v in ps[:5]], [v[2] for v in ps[:5]], s=10, c='b', marker="o", label='O')
# ax1.scatter([v[1] for v in ps[5:]], [v[2] for v in ps[5:]], s=10, c='r', marker="x", label='X')
# l = np.linspace(-2,2)
# a,b = -w[1]/w[2], -w[0]/w[2]
# ax1.plot(l, a*l + b, 'b-')
# plt.legend(loc='upper left');
# plt.show()
# # plt.savefig('./Plots.png', format='png')






# [[(1, -0.4, 0.3) 0]
#  [(1, -0.3, -0.1) 0]
#  [(1, -0.2, 0.4) 0]
#  [(1, -0.1, 0.1) 0]
#  [(1, 0.6, -0.5) 0]
#  [(1, 0.8, 0.7) 1]
#  [(1, 0.9, -0.5) 1]
#  [(1, 0.7, -0.9) 1]
#  [(1, 0.8, 0.2) 1]
#  [(1, 0.4, -0.6) 1]]