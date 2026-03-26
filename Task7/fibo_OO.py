#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#6.14

class Fibonacci():
    """Class for calculating Fibonacci sequence"""
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.x=[0,1]
       
   
    def Nterm(self):
         if (self.N) == 0:   #accounts for if user wants N=0 or N==1
            self.x = []
         elif self.N == 1: 
            self.x = 0
         else:
            while len(self.x) < self.N:  # creates a fibo sequence that is N long
                y = self.x[-1] + self.x[-2]
                self.x.append(y)
         return(self.x[-1])
    
    def Mdivisible(self):
        x_m = []
        for i in self.x:
            if (i) % self.M == 0:    #checks if element is divisible by M
                x_m.append(i)  #adds to list if yes
       
            
        return(x_m)

fibon = Fibonacci(100,7)
fibon_Nterm = fibon.Nterm()
fibon_Mdivisible = fibon.Mdivisible()
print(f"Test (N=100, M=7):")
print(f"100-th term: {fibon_Nterm}")
print(f"Terms divisible by 7: {fibon_Mdivisible}")

