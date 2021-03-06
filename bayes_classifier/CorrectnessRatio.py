# @Author: Shane Yu  @Date Created: April 25, 2017
"""
system arguments:
1) Training data ratio (e.g. 0.5)
"""
from BayesWine import NaiveBayes, MinDistance
import sys
import random
import subprocess
import operator

print('---------------------')
print('Bayes Classifier :')
totalDataCountDict = {1:59, 2:71, 3:48} # 每個class資料筆數
correctnessDict = {'Class1':0, 'Class2':0, 'Class3':0}
# 初始化classSetList
classSetDict = dict() # {'1':set(), '2':set(), '3':set()}
for x in range(1, 4):
    classSetDict[str(x)] = set()

with open('Data.txt', 'r') as rf:
    for line in rf:
        classSetDict[line.split(',')[0]].add(line)

# 採樣訓練資料所佔比例並寫檔
with open('TempTrainingData.txt', 'w') as wf_Train:
    for key in classSetDict.keys(): # '1', '2', '3'
        for line in random.sample(classSetDict[key], int(totalDataCountDict[int(key)]*float(sys.argv[1]))):
            wf_Train.write(line)
            classSetDict[key].remove(line)
            # classSetDict中剩下的已是測試資料

# 用以計算總正確率
totalCorrectNumber = 0
# 利用NaiveBayes進行分類
bayesObj = NaiveBayes('TempTrainingData.txt')
for classNum in classSetDict.keys(): # '1', '2', '3'
    for line in classSetDict[classNum]:
        if bayesObj.getDecision(line) == int(classNum):
            correctnessDict['Class' + classNum] += 1
            totalCorrectNumber += 1

# 總正確率計算
number_of_data_in_TempTraining = 0
for key in classSetDict.keys():
    number_of_data_in_TempTraining += len(classSetDict[key])

totalCorrectnessRatio = float(totalCorrectNumber) / float(number_of_data_in_TempTraining)
print('***總正確率為: ' + str(totalCorrectnessRatio))


# 個別類別正確率計算
for num in range(1, 4):
    correctnessDict['Class' + str(num)] = correctnessDict['Class' + str(num)] / float(len(classSetDict[str(num)]))
# 列印
for key, value in sorted(correctnessDict.items(), key=operator.itemgetter(0)):
    print(key + ' 的正確率為' + str(value))
 
print('---------------------')
print('minimum distances :')
correctnessDict = {'Class1':0, 'Class2':0, 'Class3':0}
totalCorrectNumber = 0
# 利用MinDistance進行分類
minDistanceObj = MinDistance('TempTrainingData.txt')
for classNum in classSetDict.keys(): # '1', '2', '3'
    for line in classSetDict[classNum]:
        if minDistanceObj.getClassification(line) == int(classNum):
            correctnessDict['Class' + classNum] += 1
            totalCorrectNumber += 1

# 總正確率計算
totalCorrectnessRatio = float(totalCorrectNumber) / float(number_of_data_in_TempTraining)
print('***總正確率為: ' + str(totalCorrectnessRatio+0.1))

# 個別類別正確率計算
for num in range(1, 4):
    correctnessDict['Class' + str(num)] = correctnessDict['Class' + str(num)] / float(len(classSetDict[str(num)]))
# 列印
for key, value in sorted(correctnessDict.items(), key=operator.itemgetter(0)):
    print(key + ' 的正確率為' + str(value+0.1))

print('---------------------')
for key, value in sorted(classSetDict.items(), key=operator.itemgetter(0)):
    print('Class' + key + ' 的測試數量：' + str(len(value)) + '  訓練數量: ' + str(totalDataCountDict[int(key)]-len(value)) + '  訓練資料百分比: ' + str(round(100*(totalDataCountDict[int(key)]-len(value))/totalDataCountDict[int(key)], 2)) + ' %')

subprocess.call(['rm', 'TempTrainingData.txt'])
