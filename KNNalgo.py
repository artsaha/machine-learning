import numpy as np
from collections import Counter

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import datasets, model_selection
from sklearn.neighbors import KNeighborsClassifier


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

## manhattan distance, frobenius distance

class KNN:
    def __init__(self, n_neighbors = 3):
        self.n_neighbors = n_neighbors

    def fit(self, X,y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        preds = [self.helper_pred(x) for x in X]
        return np.array(preds)

    def helper_pred(self, x):
        ## with list comprehension
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        k_ind = np.argsort(distances)[:self.n_neighbors]
        k_nearest_labels = [self.y_train[i] for i in k_ind]

        #majority_vote = Counter(k_nearest_labels).most_common()

        dict1 = {}

        for label in k_nearest_labels:
            if label in dict1:
                dict1[label] += 1
            else:
                dict1[label] = 1

        labels = list(dict1.keys())
        freqs = list(dict1.values())
        max_label = None
        for i in range(len(freqs)):
            if freqs[i] == max(freqs):
                max_label = labels[i]

        # 2 more approaches

        ## most_popular_label = max(dict1, key=dict1.get)
        """ 
        most_popular_label = None
        max_count = 0

        for label, count in dict1.items():
            if count > max_count:
                most_popular_label = label
                max_count = count
        """

        return max_label


def load_data(train_size: float):
    """
    train_size is for selecting the training part of dataset, portion between 0 and 1 (0,1)

    :param train_size:
    :return:
    """

    dataset = datasets.load_iris()
    X, y = dataset.data, dataset.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(1 - train_size), random_state=1234)
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = load_data(train_size=0.71)  ## 0.8 worked optimally

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)


knn3 = KNN(3)

knn3.fit(X_train, y_train)
preds = knn3.predict(X_test)
print(type(preds), preds.shape)

def acc(arr1, arr2):
    return np.sum(arr1 == arr2) / len(arr1)

for k in range(3, 21):
    knn = KNN(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(k, acc(y_pred, y_test))
