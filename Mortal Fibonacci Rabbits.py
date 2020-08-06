#!/usr/bin/env python
# coding: utf-8
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Fn=Fn-1+Fn-2-Fn-(m+1)
# In[8]:


n = 93                                                                        
m = 19                                                                         
fn = [1, 1]                                                               
x = 2                                                                     
while x < n:                                                              
    if x < m:                                                             
        fn.append(fn[-2] + fn[-1])                              
    elif x == m:                                        
        fn.append(fn[-2] + fn[-1] - 1)                          
    else:                                                                      
        fn.append(fn[-2] + fn[-1] - fn[-(m + 1)])
    x += 1                                                                
print(fn[-1])   

