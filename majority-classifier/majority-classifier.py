import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train = np.array(y_train)
    
    # find majority label
    values, counts = np.unique(y_train, return_counts=True)
    majority = values[np.argmax(counts)]
    
    # predict for all test samples
    return np.full(len(X_test), majority)