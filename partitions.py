# partitions and labels data for the algorithm

import csv

# create a list of lists
data = []

# reads csv into dataset
with open('stocks.csv') as stocks:
    file = csv.reader(stocks, delimiter=',')
    lines = 0
    for row in file:

        if len(row) < 7 or row[0] == 'Date':
            # maybe don't process these lines?
            pass
        else:
            nRow = []
            for i in range(len(row)):
                row[i] = row[i].replace(',','')
            data += [row]
            lines += 1
    print("Processed " + str(lines) + " lines.")

# generate features and labels
# labelSet = ['call', 'put']
# features = ['Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume'] from the 5 previous days
features = []
labels = []
for day in range(len(data) - 5):
    if float(data[day][4].replace(',','')) - float(data[day][1].replace(',','')) > 0: # then the stock price grew
        labels += ['call']
    else:
        labels += ['put']
    temp = []
    for i in range(5):
        temp += data[day + 1 + i][1:]
    features += [temp]

from sklearn import tree

# train data
trainTarget = labels[0 : int(len(labels) / 4)]
trainData = features[0 : int(len(features) / 4)]

# test data
testTarget = labels[int(len(labels) / 4) : int(len(labels) / 2)]
testData = features[int(len(labels) / 4) : int(len(features) / 2)]

clf = tree.DecisionTreeClassifier()
clf.fit(trainData, trainTarget)

predictions = clf.predict(testData)

from sklearn.metrics import accuracy_score
print('Accuracy: ' + str(accuracy_score(testTarget, predictions)))
