#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#gaussarea
#7 make is user input based
import numpy as np
import math
import scipy


A = float(input("input amplitude A:"))
x0 = float(input("input position of peak x0:"))
sig = float(input("input width of curve sigma:"))
z0 = float(input("input the offset in the y axis z0:"))

a = float(input("input lower limit of integration a:"))
b = float(input("input upper limit of integration b:"))

def gausss(x):
    return((A*np.exp(-(x-x0)**2/(2*sig**2)))+z0)

integral = scipy.integrate.quad(gausss, a, b)
print(f"the area under the curve with your bounds (a&b) is: {integral[0]}")


x = np.linspace((x0-6*sig), (x0+6*sig), 100000)
y = gausss(x)

plt.plot(x, y)


mask = (x>=a) & (x<=b)
plt.fill_between(x[mask], y[mask], color='orange', alpha=0.3, label=f"Area={integral[0]}")
plt.legend()

