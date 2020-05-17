#!/usr/bin/env python
# coding: utf-8

# #                                         Session 3: Assignment 3

# #                                        Task 1:
# 1.Write a function to compute 5/0 and use try/except to catch the exceptions.
# 

# In[4]:



def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')


# 2.  Implement a Python program to generate all sentences where subject is in ["Americans",
# "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[19]:


subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in range (1,len(subjects)+1):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            print (subjects[i-1],verbs[j],objects[k])


# In[22]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in obj] 
for sentence in sentence_list:
 print (sentence)


# # Task 2:
# 

# # 1.Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# HINT: Such a matrix with a geometric progression in each row is named for AlexandreTheophile Vandermonde.
# 

# In[23]:


import numpy as np
def gen_vander_matrix(ipvector, n, increasing=False):
    
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    
    return op_matx

print("------------OUTPUT-------------\n")

inputvector = np.array([1,2,3,4,5])
no_col_opmat = 3
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")

inputvector = np.array([1,2,4,6,8,10])
no_col_opmat = 5
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("---------------------------------------------------------------\n")
print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")

