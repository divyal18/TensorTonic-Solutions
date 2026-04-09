import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.array(points)
    centroids = np.array(centroids)
    
    # compute distances
    distances = np.linalg.norm(points[:, None] - centroids, axis=2)
    
    # assign closest centroid
    return np.argmin(distances, axis=1).tolist()