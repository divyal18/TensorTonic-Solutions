import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    '''
    for single feature
    
    w,b = 0.0 , 0.0
    X = np.array(X)
    y = np.array(y)
    n = len(X)
    for i in range(steps):
        y_pred = _sigmoid(X*w + b)
        dw = (1/n)*(y_pred - y)*X.T
        db = (1/n)*(np.sum(y_pred - y))

        w = w - (lr*dw)
        b = b - (lr*db)
    return w,b
    '''
    #For multiple Features
    b = 0.0
    w = np.zeros(X.shape[1])
    X = np.array(X)
    y = np.array(y)
    n = len(X)
    for i in range(steps):
        y_pred = _sigmoid(X@w + b)
        dw = (1/n)*(X.T@(y_pred - y))
        db = (1/n)*(np.sum(y_pred - y))

        w = w - (lr*dw)
        b = b - (lr*db)
    return w,b
    