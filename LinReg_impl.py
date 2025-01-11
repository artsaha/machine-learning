import numpy as np

class LinReg:

    def __init__(self):
        self.weights = 0
        self.bias = 0

    def fit(self, X, y):
        X = np.hstack([np.ones([X.shape[0],1]) ,X])
        # (X.T @ X )^-1 X.T @ y
        self.weights = np.linalg.inv(X.T @ X) @ X.T @ y

    def predict(self,X):
        X = np.hstack([np.ones([X.shape[0],1]), X])
        return X @ self.weights

