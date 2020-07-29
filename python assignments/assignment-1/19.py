x=[1,2,3,4,5,6]
s=input('enter the string to be prepended to each element: ')
y=[]
for i in x:
    i=str(i)
    y.append(s+i)
x=y
print(x)