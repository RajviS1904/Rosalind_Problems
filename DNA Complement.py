#!/usr/bin/env python
# coding: utf-8
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
# In[3]:


def reverse():
    str=input('Input the DNA string: ')
    strlen=len(str)
    sliced=str[strlen::-1]
    return sliced

def complement(str):
    comp=''
    for n in str:
        if n=='A':
            comp+='T'
        elif n=='T':
            comp+='A'
        elif n=='C':
            comp+='G'
        elif n=='G':
            comp+='C'
    print (comp)

complement(reverse())


# In[ ]:




