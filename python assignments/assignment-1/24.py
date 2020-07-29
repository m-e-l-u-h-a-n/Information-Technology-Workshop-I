x=[]
t=''
y=''
while t != '0':
    t=input('enter list element press 0 when done: ')
    x.append(t)
x.pop()
n=int(input('enter the number n: '))
z=[]
for i in range(1,n+1):
    for j in x:
        y=j+str(i)
        z.append(y)
print(z)