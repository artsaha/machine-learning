import numpy as np


class LogReg:
    def __init__(self, learning_rate=0.01,n_iters = 1000):
        self.n_iters = n_iters
        self.lr = learning_rate
        self.weights = 0
        self.bias = 0
        self.threshold = 0.5

    def sigmoid(self,x):
        return np.exp(x) / (np.exp(x) + 1)

    def fit(self, X, y):
        n_samples,dimensions = X.shape
        # number_of_rows,number_of_columns
        self.weights = np.zeros(dimensions)

        # numeric, optimization with gradient descent
        for _ in range(self.n_iters):
            logit = np.dot(X, self.weights) + self.bias
            predict = self.sigmoid(logit)

            ## binary cross - entropy loss

            ## MSE ( mean squared error ) loss
            ## derivative of loss function with respect to variable W (weights)
            dw = 1/n_samples * np.matmul(X.T, (predict - y))  # @
            ## derivative of loss function with respect to variable B (bias)
            db = 1/n_samples * np.sum(predict - y)

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, X):
        logit = np.dot(X, self.weights) + self.bias
        predicted = self.sigmoid(logit)
        y_hat = []

        for pred in predicted:
            if pred <= self.threshold:
                y_hat.append(0)
            else:
                y_hat.append(1)
        return y_hat


