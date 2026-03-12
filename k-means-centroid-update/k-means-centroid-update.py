import numpy as np
def k_means_centroid_update(points, assignments,k):
    """
    Compute new centroids as the mean 
    import numpy as np

def k_means_centroid_update(points, assignments, k):
    
    Compute new centroids as the mean of assigned points.
    """
    
    points = np.array(points)
    assignments = np.array(assignments)
    
    d = points.shape[1]
    centroids = []
    
    for i in range(k):
        cluster_points = points[assignments == i]
        
        if len(cluster_points) > 0:
            centroid = np.mean(cluster_points, axis=0)
        else:
            centroid = np.zeros(d)
        
        centroids.append(centroid.tolist())   # convert to list
    
    return centroids