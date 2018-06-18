# -*- coding: utf-8 -*-
"""
 ------------------------------------------------------------------------------
 Calculation of minimum runs according to wilks criteria
 
 Created by Jose Manuel Sojo: jmanuelsojo94@gmail.com   14/05/2018

 This script prints the minimum number of cases needed to fulfill Wilk's 
 criteria of aceptance depending on:
 
  - alpha: Fractile or percentage inside the confidence bounds
  - beta:  Confidence level   
  - m:     Number of allowed failures (must be even for two-sided boundaries)
    
 ------------------------------------------------------------------------------
"""

import numpy as np
import pandas as pd

from Wilks import Wilks
 
alpha = np.array([0.9 , 0.95 , 0.975, 0.99])
beta = np.array([0.69, 0.9 , 0.95 , 0.975, 0.99, 0.999])
m = [1, 2, 3, 4, 5]

N = np.zeros(( len(m), len(beta) ,len(alpha) ))

for i in range(len(m)):
    for b in range(len(beta)):
        for a in range(len(alpha)):
            k = m[i] + 1
            while ( Wilks(m = m[i], N = k, alpha = alpha[a]) < beta[b] ):
                k += 1           
            N[i,b,a] = k             
#    print('N fails = ', m[i])
#    print(N[i,:,:])
#    print('-----------------------')

alpha_h = [str(a*100)+'%' for a in alpha]
alpha_h[0] = 'alpha '+alpha_h[0]

beta_h = ['     '+str(b*100)+'%' for b in beta]
beta_h[0] = 'beta '+beta_h[0][5:]

m_h = ['Nfail: '+str(i)+'  ' for i in m]
    
Nt = pd.Panel( np.array([N[:,:,i] for i in range(len(alpha))]) , items = alpha_h, major_axis = m_h, minor_axis = beta_h, dtype = int)
print(Nt.to_frame())