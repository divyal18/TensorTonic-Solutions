def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    set1 = set(recommended[:k])
    set2 = set(relevant)
    n = len(relevant)
    p = len(set1.intersection(set2))/k
    r = len(set1.intersection(set2))/n
    a = [p,r]
    return a