def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    result = []
    
    for avg_rating, num_vote in items:
        denom = num_vote + min_votes
        
        if num_vote == 0:
            WR = global_mean
        else:
            WR = ((num_vote * avg_rating) + (min_votes * global_mean)) / denom
        
        result.append(float(WR))
    
    return result
    