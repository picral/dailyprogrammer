# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:35:58 2017

@author: User
https://www.reddit.com/r/dailyprogrammer/comments/x0v3e/7232012_challenge_80_easy_anagrams/
"""




def family_finder(subject):
    subject = sorted(subject.strip().lower())
    result =[]
    file = open('dictionary.txt')
    
    for w in file:
        if sorted(w.strip().lower()) == subject and len(sorted(w.strip())) == len(subject):
            result.append(w.strip())
    file.close()
    return result
        
def longest_family_finder():
    file = open('dictionary.txt')
    longest = []
    temporary = []
    for w in file:
        temporary = family_finder(w)
        longest = max(longest,temporary)
    print(longest)

    
print(family_finder('post'))
print(family_finder('bear'))