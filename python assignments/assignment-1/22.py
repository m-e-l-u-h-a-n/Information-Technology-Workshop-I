x=[]
t=1
while t != 0:
    t=int(input('enter list element press 0 when done: '))
    x.append(t)
x.pop()
for i in x:
    print(i,end='')