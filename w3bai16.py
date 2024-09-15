# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:57:02 2024

@author: Admin
"""

def print_binary(n):
    binary = bin(n)[2:]
    print(binary)

n = int(input("Nhập số nguyên dương n: "))

if n > 0:
    print_binary(n)
else:
    print("Vui lòng nhập một số nguyên dương.")