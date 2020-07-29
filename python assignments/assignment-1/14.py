from array import *
x=array('i',[1,2,3,4,1,5,1,6,2,3,1,5,10,25,5,2,221,2,3,4,1,5,1,6,2,3,1,5,10,3,1,5,10,25,5,2,2])
s=int(input('enter the number whose occurence is to be counted: '))
print(s,' occurs ',x.count(s),' times in the array')