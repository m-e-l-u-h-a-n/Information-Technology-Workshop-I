"""assuming that user enters equal number of elements in both the list"""
from collections import defaultdict
x=int(input('enter the number of elements to be kept in the list: '))
a=list()
b=list()
c=defaultdict(set)
for i in range(x):
    a.append(input('enter an element of first list: '))
    b.append(input('enter an element of second list: '))
    c[a[i]]=(b[i])
print(c)