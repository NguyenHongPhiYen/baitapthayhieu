# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:58:47 2024

@author: Admin
"""

n=1000000
total= 0.0
#câu a
for i in range(1, n+1):
    total += 1 / (i*i)
#câu b
for i in range(1, n+1):
    total += 1.0 / i*i
#câuc
for i in range(1, n+1):
    total += 1.0 / (i*i)
#câud
for i in range(1, n+1):
    total += 1 / (1.0*i*i)
