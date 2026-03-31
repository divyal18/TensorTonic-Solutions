import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    Works for a single vector [x, y, z] or an array of vectors (N, 3).
    """
    v = np.asarray(v, dtype=float)
    
    # Compute the Euclidean norm (L2 norm)
    # axis=-1 ensures it works for both 1D and 2D arrays
    norm = np.linalg.norm(v, axis=-1, keepdims=True)
    
    # Avoid division by zero: if norm is 0, return the zero vector
    # Otherwise, divide the vector by its length
    return np.divide(v, norm, out=np.zeros_like(v), where=norm != 0)