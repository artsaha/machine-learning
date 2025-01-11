import numpy as np

class LinearReg:

    def __init__(self, learning_rate=0.01,n_iters = 1000):
        self.n_iters = n_iters
        self.lr = learning_rate
        self.weights = 0
        self.bias = 0

    def fit(self, X, y):
        n_samples,dimensions = X.shape
        # number_of_rows,number_of_columns

        self.weights = np.zeros(dimensions)

        for _ in range(self.n_iters):
            y_hat = np.dot(X, self.weights) + self.bias
            # y_h = X @ self.weights + self.bias
            # y_h2 = self.weights.T @ X + self.bias

            dw = 1/n_samples * np.dot(X.T, (y_hat - y))
            db = 1/n_samples * np.sum(y_hat - y)

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, X):
        y_hat = np.dot(X, self.weights) + self.bias
        return y_hat


