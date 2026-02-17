from sklearn.linear_model import LinearRegression

import numpy as np
 ##training 
def train():
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([5, 7, 9, 11, 13])

    model = LinearRegression()
    model.fit(X, y)

    return model
