# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:08:42 2017

@author: User

Write a function that transforms a string into title case.
 This mostly means: capitalizing only every first letter of every
 word in the string. However, there are some non-obvious exceptions
 to title case which can't easily be hard-coded. Your function must accept,
 as a second argument, a set or list of words that should not be capitalized.
 Furthermore, the first word of every title should always have a capital leter.
"""

#Turns a sentence in str format to title case. Exceptions to capitalization must be included in list

def title_case(title, exceptions):
    title = list(title.lower().split(' '))
    for i,v in enumerate(title):
        if i == 0: # handles first word caps rule
            title[i] = v[0].upper() + v[1:]
        else:# handles all other exceptions in arr
            if v not in exceptions:
                title[i] = v[0].upper()+v[1:]
    print (' '.join(title))
        
title_case('the quick brown fox jumps over the lazy dog', ['jumps', 'over','the'])