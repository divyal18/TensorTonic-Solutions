import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    a = np.array(x)
    b = np.array(q)
    result = np.percentile(a,b, axis=None, out=None, method='linear', keepdims=False)
    return result
