# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:40:55 2024

@author: Admin
"""

n = int(input("Nhập số nguyên n: "))

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print() 