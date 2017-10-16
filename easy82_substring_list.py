# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:38:06 2017

@author: User

Write a function that takes a number n as an argument and returns (or outputs) 
every possible unique substrings (not counting "") of the first n letters of 
the alphabet (in any order you like).
"""

def substring(n):
    #Sanitizes the input
    if n > 26 or n < 1:
        print('alphabet only has 26 letters')
        return
    arr = []
    for i in range(97,(97+n)):
        arr.append(chr(i))
        
    for i in range(n+1):
        for j in range(i+1,n+1):
            string = ''
            for k in arr[i:j]:
                string += k
            print(string)

    
    
substring(26)
    