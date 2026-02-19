#!/usr/bin/env python
# coding: utf-8

# In[3]:


M1 = float(input("enter the month of your birthday (1 to 12):"))        
D1 = float(input("enter the day of your birthday:"))      
Y1 = float(input("enter the gregorian calendar year of your birthday:"))     

M2 = float(input("enter the month of the current date(1 to 12):"))        
D2 = float(input("enter the day of the current date:"))      
Y2 = float(input("enter the gregorian calendar year of the current date:"))   


JD_1 = 367*Y1 - 7*(Y1+(M1+9)/12)/4 - 3*((Y1+(M1-9/7))/(100+1))/4 + (275*M1)/9 + D1 + 1721029 - 0.5
# gives initial date 

JD_2 = 367*Y2 - 7*(Y2+(M2+9)/12)/4 - 3*((Y2+(M2-9/7))/(100+1))/4 + (275*M2)/9 + D2 + 1721029 - 0.5
# gives secondary date

difference_days = JD_2-JD_1 
diff_days = round(difference_days)

print(f"You are {diff_days} days old")


# 
