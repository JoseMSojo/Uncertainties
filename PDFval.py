# -*- coding: utf-8 -*-

def pdfval(dist,a,b):
    """
    Function to calculate differen probability distributions
    
    Author: Jose Manuel Sojo Gordillo: Jmanuelsojo94@gmail.com
    Created on Wed May 23 2018
    
    Inputs
    ------
    dist: String naming the distribution function: normal, lognormal or uniform

    a: Mean value of the distribution
    
    b: Interval error   
    
    Output
    ------
    parameter: Random number generated
    
    """
    from numpy import random, percentile
    parameter = - 1.0e10
    
    if dist == 'normal':
       Max = a + 2*b
       Min = max(a - 2*b, 0)
       while (parameter < Min or parameter > Max):  # Cortar las colas 95%
             parameter = random.normal(a,b,None)
             
    elif dist == 'lognormal':
         s = random.lognormal(a, b, 10000) 
         Max = percentile(s,95)
         Min = percentile(s,5)
         while (parameter < Min or parameter > Max): # Cortar las colas 90%
             parameter = random.lognormal(a,b,None)
             
    elif dist == 'uniform':
         parameter = random.uniform(a - b, a + b, None) # a +- b
    
    else:
         raise NameError(' Distribution name not recognized ')
         
    return parameter