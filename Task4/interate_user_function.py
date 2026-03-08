#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2 user input
import numpy as np
from numpy import sin, cos, exp, pi
import math
import scipy


try:
    a = eval(input("input lower bound:"))
    b = eval(input("input upper bound:"))
except Exception:
    print("you inputted something wrong, try again!")

N=100000

x = np.random.uniform(a,b, N)


try:
    func = input("input function in python (in terms of x):")
    function = lambda x: eval(func)  
    integral_s = scipy.integrate.quad(function, a, b)
    print(f"the scipy derived integral to your function is: {integral_s[0]}")
    integral_m = ((b-a)/N)*sum(function(x))         #integral w monte carlo
    print(f"the monte carlo integral is: {integral_m}")

except Exception:
    print("you inputted something wrong, try again!")

