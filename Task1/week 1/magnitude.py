#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sirius data
apparentMagnitude = float(input("Input apparent magnitude:  "))
absoluteMagnitude = float(input("Input absolute magnitude:  "))

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
print(f"the distance is {d} pc")


# In[ ]:




