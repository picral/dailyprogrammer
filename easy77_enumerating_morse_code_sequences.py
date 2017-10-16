# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:43:16 2017

@author: User

Your task is to write a function called Morse(X) which generates all morse code
 sequences of size X and returns them as an array of strings (so Morse(5)
 should return the 8 strings I just mentioned, in some order).
Use your function to generate and print out all sequences of size 10.

"""
from itertools import combinations, permutations

'''def translator(arr):
    

def Morse(x):
    sequence = []
    total = 0
    while total < x:'''
def Morse(x):        
    arr = []
    solution =[]   
    for i in range(x+1):
        for j in range((x//2)+1):
            if i*1+j*2 == x:
                t = ('.'*i+'-'*j)    
                for k in list(permutations(t)):
                    if k not in arr:
                        arr.append(k)
                        solution.append(''.join(k))


    print(solution,len(arr))
        
        