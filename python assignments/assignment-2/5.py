lst=[(),(),("",),('a','b'),('a','b','c'),('d',)]
x=len(lst)
l=[]
print(type(lst[x-1]))
for i in range(x):
    if isinstance(lst[i], tuple) and len(lst[i]) > 0:
        l.append(lst[i])
print(l)