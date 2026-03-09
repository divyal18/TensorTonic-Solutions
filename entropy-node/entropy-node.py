import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    n = len(y)
    a = np.bincount(y)
    p0 = a/n
    p0 = p0[p0 > 0]
    h = -np.sum(p0 * np.log2(p0))
    return h
    