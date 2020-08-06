#!/usr/bin/env python
# coding: utf-8

# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# 
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# 
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# 
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# 
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# In[10]:


def gc_content():
    import Bio
    from Bio import SeqIO
    file=input("Enter the name of your file: ")
    fh= open(file,'r')
    parser = SeqIO.parse(fh, "fasta")

    for record in parser:
        c=0
        a=0
        g=0
        t=0
        for x in str(record.seq):
            if "C" in x:
                c+=1    
            elif "G" in x:
                g+=1
            elif "A" in x:
                a+=1    
            elif "T" in x:
                t+=1
        gc_content=(g+c)*100/(a+t+g+c)
        dict=[record.id, gc_content]
        print(dict)
gc_content()



    


# In[15]:


import Bio

The following code only prints the Highest GC value from all the fasta sequences.
# In[12]:


from Bio import SeqIO
from Bio.SeqUtils import GC
GCcont = 0
GCname = ""
file = open("example.txt", "r")
for record in SeqIO.parse(file, "fasta"):
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
        GCname = record.id

print (GCname)
print (round(GCcont,2), "%")


# In[ ]:




