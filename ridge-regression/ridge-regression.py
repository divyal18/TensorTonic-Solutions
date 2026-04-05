def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    x = np.array(X)
    Y = np.array(y)
    return np.linalg.inv(x.T@x+lam*np.identity(x.shape[1]))@x.T@Y