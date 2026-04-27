import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    Return None for invalid input.
    """
    
    try:
        X = np.array(X, dtype=float)
    except:
        return None
    
    # must be 2D
    if X.ndim != 2:
        return None
    
    N, D = X.shape
    
    # need at least 2 samples
    if N < 2:
        return None
    
    # compute mean
    mean = np.mean(X, axis=0)
    
    # center data
    X_centered = X - mean
    
    # covariance
    cov = (X_centered.T @ X_centered) / (N - 1)
    
    return cov