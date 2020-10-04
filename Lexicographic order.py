#!/usr/bin/env python
# coding: utf-8
Organizing Strings

When cataloguing a collection of genetic strings, we should have an established system by which to organize them. The standard method is to organize strings as they would appear in a dictionary, so that "APPLE" precedes "APRON", which in turn comes before "ARMOR".

Problem

Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
# In[24]:


from itertools import combinations_with_replacement
a=input("Enter the symbols: ")
n=input("Enter the number: ")
n=int(n)
l = list(a.split(" "))
l.sort()
perm=combinations_with_replacement(l, n)
for i in perm:
    print(' '.join(map(str, (i))))


# In[8]:


from itertools import product  
N = 2
res = list(product(range(1, N + 1), repeat = N))  
print("Tuple Combinations till N are : " + str(res)) 


# In[15]:


def toString(List): 
    return ''.join(List) 

def allLexicographicRecur (string, data, last, index): 
    length = len(string) 
  
    # One by one fix all characters at the given index and 
    # recur for the subsequent indexes 
    for i in xrange(length): 
  
        # Fix the ith character at index and if this is not 
        # the last index then recursively call for higher 
        # indexes 
        data[index] = string[i] 
  
        # If this is the last index then print the string 
        # stored in data[] 
        if index==last: 
            print (toString(data))
        else: 
            allLexicographicRecur(string, data, last, index+1) 
  
# This function sorts input string, allocate memory for data 
# (needed for allLexicographicRecur()) and calls 
# allLexicographicRecur() for printing all permutations 
def allLexicographic(string): 
    length = len(string) 
  
    # Create a temp array that will be used by 
    # allLexicographicRecur() 
    data = [""] * (length+1) 
  
    # Sort the input string so that we get all output strings in 
    # lexicographically sorted order 
    string = sorted(string) 
  
    # Now print all permutaions 
    allLexicographicRecur(string, data, length-1, 0) 
  
# Driver program to test the above functions 
string = "ABC"
print("All permutations with repetition of " + string + " are:")
allLexicographic(string) 


# In[25]:


from itertools import combinations_with_replacement
a=input("Enter the symbols: ")
n=input("Enter the number: ")
n=int(n)
l = list(a.split(" "))
l.sort()
perm=combinations_with_replacement(l, n)
for i in perm:
    print(' '.join(map(str, (i))))


# In[ ]:





# In[ ]:




