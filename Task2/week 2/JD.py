#!/usr/bin/env python
# coding: utf-8

# In[14]:


# date is january 4 1700
M = 1       #month is jan
D = 4       #day is the 4th
Y = 1700    #year is 1700


JD = 367*Y - 7*(Y+(M+9)/12)/4 - 3*((Y+(M-9/7))/(100+1))/4 + (275*M)/9 + D + 1721029 - 0.5
# gives and prints the julian date

print(JD)


# 
