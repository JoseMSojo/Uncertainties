# -*- coding: utf-8 -*-

def Wilks(m, N, alpha):
    """
    Function that calculates the confidence level that a new random case will
    be inside the fractile alpha selected given the number of cases run.
    
    Author: Jose Manuel Sojo Gordillo: Jmanuelsojo94@gmail.com
    Created on Fri May 11 2018
    
    Reference:
    ----------
    Wallis, G. B. (2007). Uncertainties and probabilities in nuclear reactor regulation.
    Nuclear Engineering and Design, 237(15–17 SPEC. ISS.), 1586–1592. 
    https://doi.org/10.1016/j.nucengdes.2006.12.013
    
    Inputs
    ------
    alpha: Fractile or percentage inside the confidence bounds

    m: Number of allowed failures (must be even for two-sided boundaries)
    
    n: Number of successes    
    
    Output
    ------
    beta: Confidence level    
    
                  m          (N-i)            i        N!
    beta < 1 - Sum      alpha      * (1-alpha)  * -----------
                  i=0                             i! * (N-i)!
    
    N = n+m is the smallest integral value that will satisfy the inequality
    """
    from scipy.special import binom    # from math import factorial as fac

    if(m > N):
        raise NameError(' m > N ')
    beta = 1
    for i in range(0,m):
        # when m = 0 -> -alpha^N
        beta -=  alpha**(N-i) * (1-alpha)**i * binom(N,i)  # = fac(N)//(fac(i)*fac(N-i))
    
    return beta
