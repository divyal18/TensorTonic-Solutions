import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    x = np.array(X,dtype = float)
    Y = np.array(y, dtype = float)
    weight = np.linalg.inv(x.T@x)@x.T@Y
    return weight