#!/usr/bin/env python
# coding: utf-8
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
# In[2]:


def rna(str):
    d=dict()
    r=''
    for n in str:
        if n is 'T':
            r += 'U'
        else:
            r += n
    print('The RNA sequence is:',r)

a=str(input("Insert a DNA sequence to transcribe into RNA: "))


rna(a)


# In[ ]:




