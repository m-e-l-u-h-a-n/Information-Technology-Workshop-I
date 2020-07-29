from array import *
arr=array('i')
arr=[1,2,3,4,5,6,7,8,9]
print('before any removal',arr)
s=int(input('enter the index to be remeved: '))
for i in range(s,len(arr)-1):
    arr[i]=arr[i+1]
arr.pop();
print('after the removal',arr)