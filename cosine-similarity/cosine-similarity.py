import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    x = np.array(a)
    y = np.array(b)
    dot_product = np.dot(x,y)
    mag_x = np.linalg.norm(x)
    mag_y = np.linalg.norm(y)
    if mag_x == 0 or mag_y == 0:
        return 0
    return dot_product/((mag_x*mag_y))