#!/usr/bin/env python
# coding: utf-8
Problem

Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s(see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
# In[2]:


import re
s = input("Enter the first string: ")
t = input("Enter string to search: ")
if (s.find(t) != -1): 
    print ("Contains given substring ") 
else: 
    print ("Doesn't contains given substring") 
res = [i.start() for i in re.finditer(t, s)] 
print(res)


# In[3]:


import re 
  
# Initialising string 
ini_string = 'GATATATGCATATACTT'
  
# Initialising sub-string 
sub_string = 'ATAT'
  
# Printing initial string and sub-string 
print ("initial_strings : ", ini_string, "\nsubstring : ", sub_string) 
  
res = [] 
# Finding all occurrences of substring 
# in a string using re.finditer 
res = [m.start() for m in re.finditer(sub_string, ini_string)] 
  
# printing result( 
print ("resultant positions", str(res)) 


# In[ ]:




