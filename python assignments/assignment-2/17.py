lst=input('enter a multiword string: ').split()
s=''
x=len(lst)
for i in range(x-1,-1,-1):
    s+=(' '+lst[i])
print(s)