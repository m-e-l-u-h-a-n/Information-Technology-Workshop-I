"""i have applied selection sort algorithm on the second element of tuple"""
t=tuple()
lst=[]
t=int(input('enter the number of tuples: '))
x=str()
y=float()
for i in range(t):
    x=input('enter first element of the tuple: ')
    y=float(input('enter second element of the tuple: '))
    lst.append((x,y))
mi=int()
for i in range(t):
    mi=i
    for j in range(i+1,t):
        if lst[j][1]<lst[i][1]:
            mi=j
    lst[i],lst[mi]=lst[mi],lst[i]
print(lst)