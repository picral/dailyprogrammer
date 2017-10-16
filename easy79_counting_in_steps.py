# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:27:19 2017

@author: User

Write a function step_count(a, b, steps) that returns a list or array
 containing steps elements, counting from a to b in steps of an equal size.
 steps is a positive integer greater than or equal to 2, a and b are floating
 point numbers.

"""

def step_counter(a,b,steps):
    stepsize = (b-a)/(steps-1)
    print( [a+stepsize*i for i in range(steps)])



step_counter(18.75, -22.00, 5)
step_counter(-5.75, 12.00, 5)
step_counter(13.50, -20.75, 3)
step_counter(9.75, 3.00, 9)
step_counter(2,9,4)
step_counter(9,2,4)