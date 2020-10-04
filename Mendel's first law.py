#!/usr/bin/env python
# coding: utf-8
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
# In[3]:


# Import comb (combination operation) from the scipy library 
from scipy.special import comb

def calculateProbability(k, m, n):
    # Calculate total number of organisms in the population:
    totalPop = k + m + n 
    # Calculate the number of combos that could be made (valid or not):
    totalCombos = comb(totalPop, 2)
    # Calculate the number of combos that have a dominant allele therefore are valid:
    validCombos = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    probability = validCombos/totalCombos
    return probability

print(calculateProbability(19, 20, 24))


# In[ ]:




