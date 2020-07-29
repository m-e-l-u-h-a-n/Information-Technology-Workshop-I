lst1=[]
lst2=[]
t=1
while t != 0:
    t=int(input('enter list1 element press 0 when done: '))
    lst1.append(t)
lst1.pop()
t=1
while t != 0:
    t=int(input('enter list2 element press 0 when done: '))
    lst2.append(t)
lst2.pop()
for (i,j) in zip(lst1,lst2):
    print(i,' ',j)