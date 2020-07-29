from random import *
lo=1000000000
hi=9999999999
x=[randint(lo,hi) for i in range(100)]
"""one can verify that x is a list havin 100 lottery numbers by printing len(x) or x 
i am only printing the output asked in the question"""
y=choices(x,k=2)
print(y)