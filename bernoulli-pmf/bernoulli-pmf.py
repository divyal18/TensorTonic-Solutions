import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    
    a = np.array(x)
    mean = p
    var = p*(1-p)
    result_pmf = np.where(a == 1 , mean ,1-p)
    final_ressult = (result_pmf,float(mean),float(var))
    return final_ressult