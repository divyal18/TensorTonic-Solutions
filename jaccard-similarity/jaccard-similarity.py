def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    sset_a = set(set_a)
    sset_b = set(set_b)
    a = sset_a.intersection(sset_b)
    b = sset_a.union(sset_b)
    if len(b) == 0:
        return 0
    c = len(a)/len(b)
    return c