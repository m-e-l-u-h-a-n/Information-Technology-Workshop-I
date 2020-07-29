from array import *
s1=int(input('enter the size of first array: '))
s2=int(input('enter the size of second array: '))
arr=array('i')
print('enter the elements of the first array')
for i in range(0,s1):
    x=int(input())
    arr.append(x)
brr=array('i')
print('enter the elements of the second array')
for i in range(0,s2):
    x=int(input())
    brr.append(x)
x=list(arr)
x.sort()
y=list(brr)
y.sort()
print('x= ',x)
print('y= ',y)
z=[]
z=sorted(x+y)
print(z)