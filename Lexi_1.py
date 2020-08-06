#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
print(lexi)
lexi1=(list(set(lexi)))
sorted=lexi1.sort()
print(sorted)
#print(' '.join(map(str, (i))))


# In[ ]:




