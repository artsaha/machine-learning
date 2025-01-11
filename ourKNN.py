import numpy as np
from collections import Counter

from sklearn.model_selection import train_test_split
from sklearn import datasets, model_selection
from sklearn.neighbors import KNeighborsClassifier

class KNN:
    def __init__(self, k = 3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):  #  X is not x from math, X are points, which describe our target variable, X = [(1,2), (3,5), (6,7)]
        self.X_train = X
        self.y_train = y  ## for example color categories are in this "y"

    def predict(self,X):
        y_pred = [self.helper_pred(x) for x in X ]  # list comprehension
        return y_pred

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1-x2)**2))         ## x1 = [0,2] x2 = [1,2]  x1 - x2 = [-1, 0]  , (x1-x2)**2 = [1,0], 1+0 = 1, sqrt(1) = 1

    ## frobenius distance, mahalanobis distance, etc.

    def helper_pred(self, x):

        distances = [self.euclidean_distance(x, x_t) for x_t in self.X_train]
        indices = np.argsort(distances)[:self.k]

        labels = [self.y_train[index] for index in indices]  ## self.y_train[indices]

        dict1 = {}

        for label in labels:
            if label in dict1:
                dict1[label] += 1
            else:
                dict1[label] = 1

        most_popular_label = None
        max_count = 0

        for label, count in dict1.items():
            if count > max_count:
                most_popular_label = label
                max_count = count
    ## labels = ["red", "red", "green", "blue"]
        return most_popular_label




