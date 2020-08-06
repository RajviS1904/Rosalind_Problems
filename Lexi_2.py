#!/usr/bin/env python
# coding: utf-8

# In[19]:


from itertools import combinations_with_replacement
from itertools import permutations
a=input("Enter the symbols: ")
n=input("Enter the number: ")
n=int(n)
l = list(a.split(" "))
l.sort()
perm=permutations(l, n)
lexi=[]
for i in perm:
    lexi.append(i)
#print(lexi)
comb=combinations_with_replacement(l, n)
for i in comb:
        lexi.append(i)
lexi.sort()
#print(lexi)
y = []
for x in lexi:
    if not x in y:
        y+=[x]
#print(y)
y.sort()
for i in y:
    print(''.join(map(str, (i))))


# In[ ]:




