import numpy as np

def sigmoid(x):
    return 1/ (1+ np.exp(-x))

class LogisticRegr:

    def __init__(self, max_iter=100, alpha=0.01):
        self.alpha = alpha
        self.max_iter = max_iter
        self.weights = None
        self.bias = None

    def fit(self,X,y):
        n,d = X.shape

        self.weights = np.zeros(d)
        self.bias = 0

        ## the same gradient descent as we used in linear regression
        for _ in range(self.max_iter):
            logits = X @ self.weights + self.bias
            y_pred = sigmoid(logits)

            ## now derivatives of loss function
            dw = (1/n) * (X.T @ (y_pred - y))
            db = 1/n * (np.sum(y_pred - y))

            self.weights -= self.alpha * dw
            self.bias -= self.alpha * db


    def predict(self,X):
        logits = X @ self.weights + self.bias
        y_pred = sigmoid(logits)
        ## list comprehension
        found_class = [0 if monster<= 0.5 else 1 for monster in y_pred]
        return found_class
