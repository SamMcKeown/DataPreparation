## See dataCleaningFunctions notebook for function guide

# Libraries
import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold

# Function 1
def loadFile(text_file):
    return(np.loadtxt(text_file, delimiter=','))

# Function 2 
def colValTotal(data):
    for i in range(data.shape[1]):
        x, y = i, len(np.unique(data[:, i]))
        print('{%i: %i}' % (x, y), end=' ')
        
# Function 3 
def colValTotalLow(data):
    for i in range(data.shape[1]):
        x, y = i, len(np.unique(data[:, i]))
        if y <= 5:
            # print('> Column index: %i > Value count: %i' % (x, y))
            print('{%i: %i}' % (x, y), end=' ')
        
# Function 4
def colValPercentages(data):
    for i in range(data.shape[1]):
        x, y = len(np.unique(data[:, i])), (float(len(np.unique(data[:, i]))) / data.shape[0] * 100)
        print('{%i: %i, %.1f%%}' % (i, x, y), end=' ')
        
# Function 5
def colValPercentagesLow(data):
    for i in range(data.shape[1]):
        x, y = len(np.unique(data[:, i])), (float(len(np.unique(data[:, i]))) / data.shape[0] * 100)
        if y <= 5:
            print('{%i: %.1f%%}' % (i, y))

# Function 6
def varianceTransform(data, X, list): 
    thresholds = np.arange(0.0, 0.55, 0.05)
    for i in thresholds: 
        transform = VarianceThreshold(threshold=i)
        data = transform.fit_transform(X)
        num_of_features = data.shape[1]
        print('> Threshold=%.2f, Number of features=%d' % (i, num_of_features))
        list.append(num_of_features)
        
# Function 7
def duplicateRows(dataframe):
    rows_series = dataframe.duplicated()
    rows = rows_series[rows_series].index.values
    return(dataframe.style.apply(lambda x: ['background: yellow' if x.name in rows else '' for i in x], axis=1))