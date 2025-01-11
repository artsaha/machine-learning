import numpy as np
import pandas as pd

class DataLoader:

    def __init__(self, path):
        self.path = path
        self.data = None

    def read(self):
        self.data = pd.read_csv(self.path)

    def show_columns(self):
        return [col for col in self.data.columns]  # using list comprehension on an Index object of pandas

    def compute_cov(self, cols):
        return self.data[cols].cov()

    def compute_corr(self, cols):
        return self.data[cols].corr()

