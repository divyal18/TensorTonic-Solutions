import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    x = np.array(X,dtype = float)
    x_copy = x.copy()
    if x_copy.ndim == 1:
        mask = np.isnan(x_copy)
        if np.all(mask):
            value = 0
        else :
            if strategy == 'mean':
                value = np.nanmean(x_copy)
            else :
                value = np.nanmedian(x_copy)
        x_copy[mask] = value
        return x_copy

    for col in range(x_copy.shape[1]):
        column = x_copy[:,col]
        mask = np.isnan(column)
        if np.all(mask):
            value = 0
        else:
            if strategy == 'mean':
                value = np.nanmean(column)
            else:
                value = np.nanmedian(column)
        column[mask] = value
        x_copy[:,col] = column
    return x_copy
        