import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    a = np.array(x)
    b = np.array(y)
    return np.sqrt(np.sum((a-b)**2))