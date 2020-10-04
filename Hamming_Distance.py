#!/usr/bin/env python
# coding: utf-8
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
# In[7]:


def H_dist(s,t):
    h_dist=0
    for i,j in zip(s,t):
        if i==j:
            h_dist+=0
        else:
            h_dist+=1
    print(h_dist)
s=input("Enter first string: ")
t=input("Enter second string: ")

H_dist(s,t)


# In[ ]:




