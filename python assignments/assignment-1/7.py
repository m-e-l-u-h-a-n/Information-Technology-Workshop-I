"""the triangle may look slightly distorted for higher n(10 or more) because more digits occupy more spaces otherwise it
is correct and it can be easily checked using the values of n such that all the elements in the triagle are single digited
for example: n=5"""
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def ncr(n,r):
    if isinstance(n,int) and isinstance(r,int):
        if r==0:
            return 1
        elif r==1:
            return n
        else:
            return int(fact(n)/(fact(r)*fact(n-r)))
n=int(input('enter the number of lines to be printed: '))
if n==1:
    print(1)
else:
    for i in range(0,n-1):
        print(end=' ')
    print(1)
    for i in range(2, n+1):
        for j in range(0,(n-i)):
            print(end=' ')
        if i%2 == 0:
            for k in range(0,int(i/2)):
                print(ncr(i-1,k),end=' ')
            for k in range(int(i/2)-1,-1,-1):
                print(ncr(i-1,k),end=' ')
            print()
        else:
            for k in range(0,int(i/2)+1):
                print(ncr(i-1,k),end=' ')
            for k in range(int(i/2)-1,-1,-1):
                print(ncr(i-1,k),end=' ')
            print()